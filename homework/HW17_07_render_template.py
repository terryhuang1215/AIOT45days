# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request, render_template

app = Flask(__name__)

# . 代表在程式執行的當前目錄，加入這個設定讓程式知道我的 templates 在這邊
app.config['APPLICATION_ROOT'] = "."

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # 回傳 index.html 這個畫面
    
if __name__ == '__main__':
    app.debug = True
    app.run()