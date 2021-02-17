from flask import Flask, request
from flask import send_file
from datetime import datetime
import requests
import os
import glob
import json

list=[]

app = Flask(__name__)

# 給pi本地端上傳推論的結果
@app.route('/postLabel', methods=['POST'])
def postLabel():
    content = request.json
    list.append(content)
    print ("postLabel execute", datetime.now(), content)
    return "postlabel ok"

# 顯示pi本地端的推論資料list
@app.route('/list', methods=['GET'])
def lists():
    print ("list:", json.dumps(list))
    return json.dumps(list)

# 把pi本地端的推論資料list清除
@app.route('/clear', methods=['GET'])
def clear():
    print ("clear list:")
    list.clear()
    return "clear list ok"

# 把pi本地端已儲存的推論結果圖片都刪除    
@app.route('/clearImg', methods=['GET'])
def clearImg():
    print ("clearImg:")
    files = glob.glob('/opt/webcam_mask_flask/*.jpg')
    for f in files:
        print ("rm ",f)
        os.remove(f)
    return "clear images ok"

# 從pi取出一張指定推論結果圖片
@app.route("/img", methods=['GET'])
def img():
    filename = request.args.get("file")
    print ("filename:", filename)
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081, debug = True, threaded = True)

