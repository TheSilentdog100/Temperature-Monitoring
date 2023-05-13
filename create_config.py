file = open("config_Temperature_Monitoring","w")
time_intervall = input("Please enter the time interval in seconds, in which the data should be monitored\n")
file.write("reading_interval = "+time_intervall+"\n")
enable_logging = input("should logging be enabled (yes/no)\n")
file.write("enable logging = "+enable_logging+"\n")
if enable_logging=="yes":
    print("Please enter your desired logging Path (total path!)")
    logging_path = input("Example: /home/user/myloggingfile.log\n")
else:
    logging_path = "logging is disabled!"
file.write("logging path = "+logging_path+"\n")
print(f"Your desired time intervall is: {time_intervall}")
if enable_logging=="yes":
    print(f"you have enable logging and set your log file to: {logging_path}")
else:
    print("you disabled logging")
    print(f"note: this will lead to a print only statements every {time_intervall} seconds")