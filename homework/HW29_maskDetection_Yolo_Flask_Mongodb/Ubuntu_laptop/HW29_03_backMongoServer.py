from pymongo import MongoClient  
import requests
import base64
import datetime
import time
import json


url = 'http://192.168.0.100:8081' # 指定pi flask web的位址

# 連接後端 server 的 mongodb
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_mask_pred_db'] # 建立一個data base 命名為 yolo_mask_pred_db
coll = db['Collections'] #建立一個collections，透過coll變數呼叫他


def clear():
  clear_url = url+'/clear'
  r = requests.get(clear_url) # 將pi flask web server上的辨識結果與影像清除
  if r.status_code == requests.codes.ok: # 確定連接是否順利 (not 502 or 400)
      print("clear_OK")


def getImg(j, filename):   # 從flask取得推論結果
  
  # 從pi下載推論結果與圖片並儲存成一個檔案
  img_url = url+'/img?file='+filename # 指定web中影像的位址
  with open('static/'+filename, 'wb') as handle: #使用python內建的檔案讀寫工具open
        response = requests.get(img_url, stream=True)
        if not response.ok:
            print (response)

        for block in response.iter_content(1024): #將影像儲存在檔案裡
            if not block:
                break
            handle.write(block)

  # 將影像結果編碼之後，儲存在 mongodb內
  with open('static/'+filename, "rb") as f: #使用python內建的檔案讀寫工具open
    bin_pic = base64.b64encode(f.read()).decode('utf-8') # 將讀取到的圖片(f)編碼成二進制檔
    mydata = {'label':j['label'], 'x':j['x'], 'y':j['y'], 'w':j['w'], 'h':j['h'], 'img': filename, 'image_data': bin_pic}
    result = coll.insert_one(mydata) 


def fetchYoloResult():  # 從pi的flask web server上取得推論list結果
  datetime_dt = datetime.datetime.today()# 獲得當地時間
  datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期
  print ("fetchYoloResult:"+datetime_str)
  r = requests.get(url+'/list')
  if r.status_code == requests.codes.ok:
      print(r.text)

  #將 pi 上面的影像辨識結果list，轉換成json物件
  yolo_result = r.text
  yolo_json = json.loads(yolo_result)

  for j in yolo_json:
      print(j) #把每一個json物件印出來檢查
#      coll.insert_one(j) #把json物件新增到 mongodb
      img=j['img'] # 取出 json物件中影像檔案名稱
      getImg(j, img)  # 至 pi flask web server取出影像內容儲存至mongodb

  clear() # 將pi flask web server上的資料清除


while True:
	fetchYoloResult()
	time.sleep(5) # 每隔5秒抓一次資料
  