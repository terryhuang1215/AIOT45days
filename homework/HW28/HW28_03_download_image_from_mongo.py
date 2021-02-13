from PIL import Image
from io import BytesIO
from pymongo import MongoClient  
import base64


# 連接到local端的MongoDB
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_pred_db']
coll = db['Collections']

_id = "6028037aa96d1ac215ab027b"

# 尋找指定ID的圖片
img_base64 = []
for i in coll.find():
	#print(str(i['_id']))
	#print(type(i['_id']))
	if str(i['_id']) == _id:
		#print()
		img_base64.append(i['image_data'])

im = Image.open(BytesIO(base64.b64decode(img_base64[0])))
im.show()
im.save('mongoDB_image.jpg', 'JPEG')
print("download image from MongoDB: done!")
