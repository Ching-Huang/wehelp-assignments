from flask import Flask, redirect, url_for, render_template, request, session, jsonify

# 導入 JSON 模組
import json

# 連接到 MySQL 資料庫
import mysql.connector
website = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "password",
  database = "website",
)
cursor = website.cursor()

# [增]新增 1 筆會員資料到 database 中
# database => member table
def AddNewMemberToDB(name, username, password):
    sql = "INSERT INTO member (name, username, password, follower_count) VALUES (%s, %s, %s, %s)"
    member = (name, username, password, 0)
    cursor.execute(sql, member)
    website.commit()

# [查]讀取 database 資料，查詢 資料庫中有無 此帳號( username )
def SearchMemberByUsername(username):
    sql = "SELECT * FROM member WHERE username = %s"
    variable = (username, )
    cursor.execute(sql, variable)
    SearchResult = cursor.fetchall()

    '''若無 此帳號(會印出 空[])，則回傳 null ;
       反之       (會印出 值) ，則回傳 搜尋結果資料'''
    if SearchResult == []:
        print('== 無該筆會員資料 ==')
        return None
    else:
        print('== 搜尋結果如下 ==')
        for UserData in SearchResult:
            print(UserData)
        return SearchResult

# [改]修改該會員姓名(name)
def ModifyMemberNameByAccount(Account, ModifiedName):

    '''修改該會員的姓名

    修改 資料庫中帳號(欄位名稱 username )所對應的姓名(欄位名稱 name )
    
    Example :
        更改帳號 puppy 的姓名 dog 為 chocho
        ---------------------------
        | name       | username   |
        ---------------------------
        | dog        | puppy       |
        ---------------------------
            
        >>> ModifyMemberNameByAccount('puppy','chocho')       
    
    Args:
        Account     : 要修改的帳號(username)
        ModifiedName: 修改後的姓名(name)
    
    '''
    sql = "UPDATE member SET name = %s WHERE username = %s"
    variable = (ModifiedName, Account)
    cursor.execute(sql, variable)
    website.commit()
    
#建立 Flask 物件
app = Flask(__name__)

#設定 session 的密鑰
app.secret_key = "so far so good"

#網站的首頁
@app.route('/')
def index():
    MemberName = session.get("user")
    if MemberName != None:
        return redirect(url_for('success'))
    else:
        return render_template('index.html')

@app.route('/member/')
def success():
    MemberName = session.get("user")
    if MemberName == None:
        return redirect(url_for('index'))   
    else:
        return render_template('success.html', name = MemberName)
         
@app.route('/error/')
def error():
    data = request.args.get("message", None)
    return render_template('error.html', text = data)

#處理 註冊帳號 路由
@app.route('/signup', methods=['POST'])
def sign_up():
    if request.method == 'POST':

        # 讀取 新註冊會員 姓名,帳號,密碼
        SignUpName    = request.form['name']
        SignUpAccount = request.form['account']
        SignUpPwd     = request.form['pwd']

        # 搜尋 member 資料表中是否有此會員
        SearchResult = SearchMemberByUsername(SignUpAccount)
        print('搜尋 member 資料表',SearchResult)

        # 若 無 此會員，則新增資料到 member 資料表，註冊成功，導回【首頁網址】
        if SearchResult == None:
            AddNewMemberToDB(SignUpName, SignUpAccount, SignUpPwd)
            return redirect(url_for('index'))

        # 若 有 此會員，則不新增資料，註冊失敗，導向【失敗頁網址】，並顯示「帳號已經被註冊」
        else:
            return redirect(url_for('error', message = "帳號已經被註冊"))    

#處理 登入系統 路由
@app.route('/signin', methods=['POST'])
def sign_in():

    if request.method == 'POST':
        account = request.form['account']
        pwd     = request.form['pwd']

        if(account == "") or (pwd == ""):
            return redirect(url_for('error', message = "請輸入帳號、密碼"))  

        # 檢查資料庫的 member 資料表中是否有對應的帳號、密碼
        SearchResult = SearchMemberByUsername(account)
        # print('檢查資料庫',SearchResult)

        # 帳號密碼 沒有對應，登入失敗，將使用者導向【失敗頁網址】，並顯示「帳號或密碼輸入錯誤」
        if SearchResult == None:
            return redirect(url_for('error', message = "帳號、或密碼輸入錯誤"))  

        # 帳號密碼 有對應 ，將使用者姓名加入 session 中紀錄，登入成功，將使用者導向【會員頁網址】，並在頁面中顯示使用者姓名。
        else:

            # 只取出搜尋結果陣列中的第0筆
            SignInMember     = SearchResult[0]
            SignInMemberPwd  = SignInMember[3]

            # 欄位 password
            if pwd == SignInMemberPwd:
                session['user']     = SignInMember[1] # 紀錄目前登入的 使用者姓名
                session['username'] = SignInMember[2] # 紀錄目前登入的 使用者帳號
                return redirect(url_for('success')) 
            else:
                return redirect(url_for('error', message = "帳號、或密碼輸入錯誤"))  

#供 前端 使用的 API 路由 - [查詢會員資料] 
@app.route('/api/members', methods=['GET'])
def api_search():
    KeyInUsername = request.args.get("username", None)

    # 檢查資料庫的 member 資料表中是否有對應的 會員帳號
    SearchResult = SearchMemberByUsername(KeyInUsername)

    if SearchResult != None:

        # 只取出搜尋結果陣列中的第0筆
        Member       = SearchResult[0]
        # print("== Member ==", Member)

        PythonFormat = {
            "data": {
                "id": Member[0],
                "name": Member[1],
                "username": Member[2]
            }
        }

        Convert2JsonFormat = json.dumps(PythonFormat, ensure_ascii = False)
        return Convert2JsonFormat
    else:
        PythonFormat = {
            "data": None
        }

        Convert2JsonFormat = json.dumps(PythonFormat, ensure_ascii = False)
        return Convert2JsonFormat

#供 前端 使用的 API 路由 - [修改會員姓名] 
@app.route('/api/member', methods=['POST']) 
def api_modify():
    
    # 取得目前的登入帳號
    MemberName = session.get("username")

    if MemberName != None: 
        CurrentUserName = session['username']
        # print('目前使用者帳號為 = ', CurrentUserName)

    else:  # 未登入時的狀態
        Response = {"error": 'true'}
        return jsonify(Response)

    if request.method == 'POST':
        RequestBody  = request.json  # 取得前端送來的 Request Body 請求資料 
        ModifiedName = RequestBody['name']  # 取出修改後的 "新姓名"
        
        # 修改會員姓名
        ModifyMemberNameByAccount(CurrentUserName, ModifiedName)

        # 從資料庫中取得修改後的姓名 並更新 session
        SearchResult = SearchMemberByUsername(CurrentUserName)        
        session['user'] = SearchResult[0][1] #更新 session 中的姓名 

        Response = {"ok":'true'}
    return jsonify(Response)

#處理 登出系統 路由
@app.route('/signout', methods=['GET'])
def sign_out():
    if 'user' in session:
        session.clear()
    return redirect(url_for('index')) 

if __name__ == "__main__":    
    app.run(host = '127.0.0.1', port = 3000)


