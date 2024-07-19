import adafruit_dht
import time
from time import sleep
import board

# Open config file in read-only mode
with open("config_Temperature_Monitoring", "r") as config_file:
    time_interval = config_file.readline().removeprefix("reading_interval = ").removesuffix("\n")
    time_interval = int(time_interval)
    logging = config_file.readline().removeprefix("enable logging = ").removesuffix("\n")
    logging_path = config_file.readline().removeprefix("logging path = ").removesuffix("\n")

# Used to avoid problems when using crontab
# for automatic start
sleep(30)

# Initializing sensor
# DHT11 sensor connected to GPIO12.
sensor = adafruit_dht.DHT11(board.D12)
print("[press ctrl+c to end the script]")

try:  # Main program loop
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            current_time = time.asctime(time.localtime())  # Get current time
            current_time = current_time[0:-4]  # Get rid of year

            if humidity is not None and temperature is not None:
                if logging == "yes":
                    with open(logging_path, "a") as file:
                        file.write(current_time + f" Temperatur: {temperature}°C" + f", Luftfeuchtigkeit: {humidity}%\n")
                elif logging == "no":
                    print(current_time + f" Temperatur: {temperature}°C" + f", Luftfeuchtigkeit: {humidity}%")
            print("went through loop iteration")
        except RuntimeError as error:
            # Handle occasional sensor read errors
            print(f"Error reading sensor data: {error}")

        sleep(time_interval)

# Scavenging work after the end of the program
except KeyboardInterrupt:
    print("Script end!")
finally:
    sensor.exit()
