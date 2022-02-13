from flask import Flask, redirect, url_for, render_template, request, session

# 宣告全域變數記錄使用者登入名稱
CurrentLoginName  = ''

# 連接到 MySQL 資料庫
import mysql.connector
website = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "password",
  database = "website",
)
cursor = website.cursor()

# 新增 1 筆會員資料到 database 中
# database => member table
def addNewMemberToDB(name, username, password):
    sql = "INSERT INTO member (name, username, password, follower_count) VALUES (%s, %s, %s, %s)"
    member = (name, username, password, 0)
    cursor.execute(sql, member)
    website.commit()

# 讀取 database 資料，查詢 資料庫中有無 此帳號( username )
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

app = Flask(__name__)

#設定 session 的密鑰
app.secret_key = "so far so good"

#網站的首頁
@app.route('/')
def index():
    if 'user' in session and session['user'] == "Sign_In": 
        print('[index]Session key user =', session['user'])
        return redirect(url_for('success'))
    else:
        return render_template('index.html')

@app.route('/member/')
def success():
    global CurrentLoginName 
    MemberName = CurrentLoginName #將先前於 Signin 記錄的會員姓名拿來使用 
    if 'user' in session and session['user'] == "Sign_In":
        return render_template('success.html', name = MemberName)
    else:
        return redirect(url_for('index')) 
        
@app.route('/error/')
def error():
    data = request.args.get("message", None)
    return render_template('error.html', text = data)

#處理 註冊帳號 路由
@app.route('/signup', methods=['POST'])
def signup():
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
            addNewMemberToDB(SignUpName, SignUpAccount, SignUpPwd)
            return redirect(url_for('index'))

        # 若 有 此會員，則不新增資料，註冊失敗，導向【失敗頁網址】，並顯示「帳號已經被註冊」
        else:
            return redirect(url_for('error', message = "帳號已經被註冊"))    

#處理 登入系統 路由
@app.route('/signin', methods=['POST'])
def signin():

    global CurrentLoginName #引用全域變數 紀錄目前登入者姓名

    if request.method == 'POST':
        account = request.form['account']
        pwd     = request.form['pwd']

        if(account == "") or (pwd == ""):
            return redirect(url_for('error', message = "請輸入帳號、密碼"))  

        # 檢查資料庫的 member 資料表中是否有對應的帳號、密碼
        SearchResult = SearchMemberByUsername(account)
        print('檢查資料庫',SearchResult)

        # 帳號密碼 沒有對應，登入失敗，將使用者導向【失敗頁網址】，並顯示「帳號或密碼輸入錯誤」
        if SearchResult == None:
            return redirect(url_for('error', message = "帳號、或密碼輸入錯誤"))  

        # 帳號密碼 有對應 ，將使用者姓名加入 session 中紀錄，登入成功，將使用者導向【會員頁網址】，並在頁面中顯示使用者姓名。
        else:

            #只取出搜尋結果陣列中的第0筆
            SignInMember     = SearchResult[0]
            SignInMemberPwd  = SignInMember[3]

            # 欄位 password
            if pwd == SignInMemberPwd:
                session['user'] = "Sign_In"
                CurrentLoginName = SignInMember[1] # 紀錄目前登入的 使用者姓名
                return redirect(url_for('success')) 
            else:
                return redirect(url_for('error', message = "帳號、或密碼輸入錯誤"))  


@app.route('/signout', methods=['GET'])
def signout():
    if 'user' in session:
        session['user'] = "Sign_Out"
        print('[signout]Session key user =', session['user'])
    return redirect(url_for('index')) 

if __name__ == "__main__":    
    app.run(host = '127.0.0.1', port = 3000)


