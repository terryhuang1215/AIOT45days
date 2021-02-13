
from pymongo import MongoClient  
import requests
import base64


url = 'http://192.168.0.102:8081' # 指定flask web的位址
index_url = url+'/index' # 指定web中影像的位址 (影像被放在inex目錄下)

# 從flask取得推論結果
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.text)
yolo_result = r.text

# 從flask端取得影像的位址
r = requests.get(index_url) # 從影像的位址取得該頁面的內容
if r.status_code == requests.codes.ok: # 確定連接是否順利 (not 502 or 400)
    print("Get detect image: OK")
res = r.text # 取得文字內容，裡面包含影像的檔名以及位置，我們需要用這兩個資訊來取得圖片
head = res.find('<img src=') # 取得影像物件的html敘述的開頭index
tail = head+res[head:].find('>') # 取得影像物件的html敘述的結尾index
img_url = url+res[head:tail].split('\"')[1] # 透過頭尾index來取得影像的具體位址
print("img_url:", img_url)

# 下載圖片並儲存
img_name = 'prediction.jpg'
html = requests.get(img_url)
with open(img_name, 'wb') as file:
    file.write(html.content)
    print("Save image '"+img_name+"' OK")


# 將圖片和推論結果一起儲存在MongoDB中
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_pred_db'] # 建立一個data base名為test_db
coll = db['Collections'] # 在test_db中 建立一個collections名為coll
    
with open(img_name, "rb") as f: #使用python內建的檔案讀寫工具open
    bin_pic = base64.b64encode(f.read()).decode('utf-8') # 將讀取到的圖片(f)編碼成二進制檔
    mydata = {'yolo_result': yolo_result, 'image_data': bin_pic}
    result = coll.insert_one(mydata)
    print("inserted_id:", result.inserted_id) # 打印出my_data在儲存時，DB分配出來的id
