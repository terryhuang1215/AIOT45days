# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['GET'])
def index():
    # 回傳 Hello World 字串
    return "Hello World"
    

if __name__ == '__main__':
    app.run()