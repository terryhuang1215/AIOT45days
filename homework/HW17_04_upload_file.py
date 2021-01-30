# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['POST'])
def index():
    file = request.files['file'] # 取得 request 中的 file(記得發送 postman 中的 檔案參數名稱要和這邊一致)
    file.save(file.filename) # 把檔案存起來，並用原來的檔名作為名稱
    return file.filename #回傳檔案名稱
    

if __name__ == '__main__':
    app.run()