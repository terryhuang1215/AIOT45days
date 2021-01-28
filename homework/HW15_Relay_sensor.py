import Adafruit_DHT
import time
import sys
import gpiozero

RELAY_PIN = 26
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

set_temp = 20 # this is the required temperature

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))

        # test for low temperature
        if temperature < set_temp:
            print("this is were you put the code to turn on your relay")
            relay.on()

        # test for high temperature
        if temperature > (set_temp + 1):
            print("this is were you put the code to turn off your relay")
            relay.off() 
    else:
        print("Failed to retrieve data from humidity sensor")

    #this is the time between taking readings and acting on them you can reduce it but not below 5 seconds
    time.sleep(30)

