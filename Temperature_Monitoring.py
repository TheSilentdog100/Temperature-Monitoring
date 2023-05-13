import Adafruit_DHT
import time
from time import sleep

#open config file in read only mode
config_file = open("config_Temperature_Monitoring","r")
time_interval = config_file.readline().removeprefix("reading_interval = ").removesuffix("\n")
time_interval = int(time_interval)
logging = config_file.readline().removeprefix("enable logging = ").removesuffix("\n")
logging_path = config_file.readline().removeprefix("logging path = ").removesuffix("\n")



#used to avoid problems when using crontab
#for automatic start
sleep(30)

#initializing sensor
sensor = Adafruit_DHT.DHT11
#DHT11 sensor connected to GPIO12.
pin = 12
print("[press ctrl+c to end the script]")

try: # Main program loop
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        current_time = time.asctime(time.localtime()) #get current time
        current_time = current_time [0:-4] #get rid of year
        file = open(logging_path,"a")
        if humidity is not None and temperature is not None:
            if logging=="yes":
                file.write(current_time+f"Temperatur: {temperature}°C"+f", Luftfeuchtigkeit:{humidity}%\n")
            elif logging=="no":
                print(current_time+f"Temperatur: {temperature}°C"+f", Luftfeuchtigkeit:{humidity}%")
        file.close()
        sleep(time_interval)
# Scavenging work after the end of the program
except KeyboardInterrupt:
    print("Script end!")
