# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['POST'])
def index():
    files = request.files.getlist('file') # 若有多個檔案，必須使用 getlist  
    total = 0
    for file in files:
        total += 1 # 讀到一個檔案就加一
        file.save(file.filename) # 把檔案存起來，並用原來的檔名作為名稱
    
    return str(total) # 回傳總上傳的檔案數量
    

if __name__ == '__main__':
    app.run()