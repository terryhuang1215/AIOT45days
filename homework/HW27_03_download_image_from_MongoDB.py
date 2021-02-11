from PIL import Image
from io import BytesIO
from pymongo import MongoClient  
#import matplotlib.pyplot as plt
import base64


img_name = 'orange.jpg' # 這裡要替換成你要讀取的圖片的檔名


# 連接到local端的MongoDB
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['test_db']
coll = db['Collections']

_id = [] # 創建一個list
with open("imageList.txt", "r") as file: # 讀取imageList.txt文件
	lines = file.readlines() # 讀取檔案內容的每一行文字為陣列
	for i in range(len(lines)):
		if img_name in lines[i]: # 注意: 讀取到的每一列其實後面會跟著\n(換行)
			a = lines[i+1].split('\n') # 所以在這裡把\n跟想要的內容區隔開
			_id.append(a[0]) # 單獨把想要的內容存到list(_id)中
# print(_id[0]) # 你可以用這個指令來觀察你得到的內容(圖像在DB中的id)


# 尋找指定ID的圖片
img_base64 = []
for i in coll.find():
#     print(str(i['_id']))
#     print(type(i['_id']))
	if str(i['_id']) == _id[0]:
#         print()
		img_base64.append(i['orange_jpg_base64'])

im = Image.open(BytesIO(base64.b64decode(img_base64[0])))
im.show()
im.save('mongoDB_image.jpg', 'JPEG')
print("download image from MongoDB: done!")
