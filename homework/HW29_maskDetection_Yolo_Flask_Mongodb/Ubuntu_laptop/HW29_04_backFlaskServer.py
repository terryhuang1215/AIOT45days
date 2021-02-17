from flask import Flask, request
from pymongo import MongoClient
import requests


# 在後端筆電上執行, 目的是給前端使用者查詢後端mongodb寫入狀況


# static_url_path主要用於改變url的path，靜態文件放在static下面，所以正常情況url是static/filename，但可通過static_url_path來改變這個url
# static_folder主要是用來改變url的目錄，默認是static，可以通過這個變量來改變靜態文件目錄。
app = Flask(__name__, static_url_path='/static')


# 連接後端 server 的 mongodb
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_mask_pred_db'] # 建立一個data base 命名為 yolo_mask_pred_db
coll = db['Collections'] #建立一個collections，透過coll變數呼叫他

@app.route('/', methods=['GET'])
def list():
    htmlContent="<html>"
    htmlContent=htmlContent+"<head><meta http-equiv='refresh' content='10'></head>"
    htmlContent=htmlContent+"<table border=1 cellspacing=0 cellpadding=5>"
    htmlContent=htmlContent+"<tr><th>label</th><th>x</th><th>y</th>"
    htmlContent=htmlContent+"<th>w</th><th>h</th><th>filename</th><th>img</th></tr>"

    mydoc = coll.find().sort("img",-1).limit(10);
    count=1
    for i in mydoc:
        x="<tr>"
        x=x+"<td>"+str(count)+"</td>"
        x=x+"<td>"+i['label']+"</td>"
        x=x+"<td>"+str(i['x'])+"</td>"
        x=x+"<td>"+str(i['y'])+"</td>"
        x=x+"<td>"+str(i['w'])+"</td>"
        x=x+"<td>"+str(i['h'])+"</td>"
        x=x+"<td>"+i['img']+"</td>"
        x=x+"<td><img width='128' src='/static/"+i['img']+"'></td>"
        htmlContent=htmlContent+x
        x=x+"</tr>"
        count=count+1
 
    htmlContent=htmlContent+"</table></html>"
    return htmlContent

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081, debug = True, threaded = True)
