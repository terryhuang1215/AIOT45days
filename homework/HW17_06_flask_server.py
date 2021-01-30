# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request, redirect, url_for, send_file

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['POST'])
def index():
    file = request.files.get('file') # 先接收傳送過來的檔案
    file.save(file.filename) # 儲存檔案
    # 將請求導到 upload_finish，並帶入要回傳的檔案名稱
    return redirect(url_for('upload_finish', filename=file.filename))

@app.route('/upload_finish/<filename>')
def upload_finish(filename):
    return send_file(filename) # 從資料夾中拿取檔案，並回傳回去
    

if __name__ == '__main__':
    app.run()