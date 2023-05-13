#Temperature-Monitoring

Note: as far as i know this script only works
for Raspberry pi or maybe other arm devices
   
This is a simple python script to monitor the room temperature.   
Using a sensor from Adafruit_DHT.  
  
To install all the needed packages:  
pip -r install requirements.txt  
or type: pip install Adafruit_DHT  
  
then setup your config using create_config.py  
type: python3 create_config.py and follow the instructions  
  
you can then start the script using:  
python3 Temperature_Monitoring.py  
  
you can also start the script automaticaly at startup  
using other methods like crontab etc.  
  
Have fun
