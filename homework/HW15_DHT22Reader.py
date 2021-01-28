import Adafruit_DHT # 匯入Adafruit_DHT模組

DHT_SENSOR = Adafruit_DHT.DHT22 # 感測器為DHT22
DHT_PIN = 27    #設定DHT22 Data接線的接腳位置

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")


