# yolo  + Flask

import os
import sys
import time
from flask import Flask, render_template

sys.path.append('/home/pi/darknet/')

app = Flask(__name__)

input_imgpath = '/home/pi/Workspace/HW28/flask_webcam/image.jpg'
output_imgpath = '/home/pi/Workspace/HW28/flask_webcam/static/prediction.jpg'

def snapshot():
    # fswebcam --no-banner /home/pi/Workspace/HW28/flask_webcam/image.jpg
    os.system('fswebcam --no-banner '+input_imgpath)

def default_yolo():
    snapshot()
    
    path = os.getcwd()
    
    #configPath = "./cfg/yolov3_training.cfg"
    #weightPath = "./cfg/yolov3_training_last.weights"
    #metaPath= "./data/obj.data"
    
    os.chdir('/home/pi/darknet')
    #from darknet import performDetect
    #a = performDetect(imagePath=imgpath, configPath=configPath, weightPath=weightPath, metaPath=metaPath)
    os.system('./darknet detector test ./data/obj.data ./cfg/yolov3_training.cfg ./cfg/yolov3_training_last.weights '+input_imgpath+ '> infer.txt')
    
    with open("infer.txt", "r") as file:
        line = file.readlines()[7]
        line = line.strip()
        a = line.split(":")
        #print("a[0]:", a[0])
        #print("a[1]:", a[1])
    
    os.system('cp -f ./predictions.jpg '+output_imgpath)
    
    os.chdir(path)
    
    return a

def defult_display():
    ans = default_yolo()
    #text0 = 'detect: '+ans[0][0]+'\tconfidence: '\
    #    +str(format(ans[0][1], '.5f'))
    text0 = 'detect: '+ans[0]+'\tconfidence: '+ans[1]
    text1 = '\ntime is: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    reply = text0 + text1
    return reply


if __name__ == "__main__":
    
    reply = defult_display()
    
    @app.route("/")
    def abc():
        return reply

    @app.route("/index")
    def show_index():
        return render_template("index.html")

    app.run(host='0.0.0.0', port = 8081, debug = True, threaded = True)
    