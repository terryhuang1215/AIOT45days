# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['POST'])
def index():
    name = request.form.get('name') # 取得 name 參數
    return "Your name: " + name
    #passwd = request.form.get('passwd') # 取得 passwd 參數
    #return "Your name: " + name + ", Your passwd: " + passwd
    

if __name__ == '__main__':
    app.run()