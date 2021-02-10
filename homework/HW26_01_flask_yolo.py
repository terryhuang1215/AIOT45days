# yolo  + Flask
import os
import sys
import time
from flask import Flask
from darknet import performDetect

sys.path.append('/home/pi/darknet/') # 將darknet.py的位路徑加入sys
#from new_darknet import performDetect
app = Flask(__name__)


def default_yolo():
    path = os.getcwd() # 取得本文件當前位置 (可省略)
    os.chdir('/home/pi/darknet') # 移動到darknet.py的位置才能導入推論函式
    
    imgpath = '/home/pi/Downloads/orange_inference_config_file_tinyYolo/orange.jpeg' # 以下設定必要參數(參數檔案的路徑)
    configPath = "./cfg/yolov3_training.cfg"
    weightPath = "./cfg/yolov3_training_last.weights"
    metaPath = "./data/obj.data"

    a = performDetect(imagePath = imgpath, configPath = configPath,
                      weightPath = weightPath, metaPath = metaPath)
    
    os.chdir(path) #移動回本文件所在位置 (可省略)
    return a


def defult_display():
    ans = default_yolo()
    text0 = 'detect: '+ans[0][0]+'\tconfidence: '\
        +str(format(ans[0][1], '.5f'))
    text2 = '\ntime is: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    reply = text0 + text2
    return reply


if __name__ == "__main__":
    
    reply = defult_display()
    
    @app.route("/")
    def abc():
        return reply
    
    app.run(host='0.0.0.0', port = 8081, debug = True, threaded = True)
