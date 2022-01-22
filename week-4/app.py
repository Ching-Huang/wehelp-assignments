from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

#設定 session 的密鑰
app.secret_key = "so far so good"

#網站的首頁
@app.route('/')
def index():
    if 'user' in session and session['user'] == "Sign_In": 
        print('[index]Session key user =',session['user'])
        return redirect(url_for('success'))
    else:
        return render_template('index.html')

@app.route('/member/')
def success():
    if 'user' in session and session['user'] == "Sign_In":
        return render_template('success.html')
    else:
        return redirect(url_for('index')) 
        
##################################################################################
# 透過 request 取得條件判斷式所要求的字串資料 message (動態參數)，並命名為變數 data
# 樣板裡的變數名稱 text 會等同 此 動態參數
# 動態參數:選擇性的視圖函式參數
##################################################################################
@app.route('/error/')
def error():
    data = request.args.get("message", None)
    return render_template('error.html', text = data)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        account = request.form['account']
        pwd     = request.form['pwd']

        if(account == "") or (pwd == ""):
            return redirect(url_for('error', message = "請輸入帳號、密碼"))  

        #帳號密碼輸入正確
        if(account == "test") and (pwd == "test"):
            session['user'] = "Sign_In"
            return redirect(url_for('success')) 

        elif(account != "test") or (pwd != "test"):
            return redirect(url_for('error', message = "帳號、或密碼輸入錯誤"))  

@app.route('/signout', methods=['GET'])
def signout():
    if 'user' in session:
        session['user'] = "Sign_Out"
        print('[signout]Session key user =',session['user'])
    return redirect(url_for('index')) 

if __name__ == "__main__":    
    app.run(host = '127.0.0.1', port = 3000)


