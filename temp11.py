import pymysql, threading, time
#import serial
conn = pymysql.connect(
    host="mydbinstance.c83ecbfiopy9.ap-south-1.rds.amazonaws.com",
    passwd="project123",
    port = 3306, 
    user="Berlin199",
    database ="mydatabase",
)
mycursor = conn.cursor()

#mycursor.execute("CREATE TABLE temperature (sid INT AUTO_INCREMENT PRIMARY KEY, readings INT)")
#mycursor.execute("CREATE TABLE pulse (sid INT AUTO_INCREMENT PRIMARY KEY, readings INT)")
#mycursor.execute("CREATE TABLE ECG (sid INT AUTO_INCREMENT PRIMARY KEY, readings INT)")

# list for all 3 readings
p_list = []
t_list = []
e_list = []
report_complete = False

def timeFunction():
	time.sleep(10)	#enter time in seconds in sleep() for report total time
	report_complete = True


threading.Thread(target = timeFunction).start()

while 1:
	if not report_complete:
	    ser = serial.Serial('/dev/ttyACM0', 9600)
	    if not report_complete:
		    while True:
		        read_serial = ser.readline()
		        pulse, temp, ecg = read_serial.split("/")
		        ecg, waste = ecg.split("\r")

		        p_list.append(pulse)
		        t_list.append(temp)
		        e_list.append(ecg)
		else:
			break
	else:
		break

print('pulse readings: ',p_list)
print('temperature readings: ',t_list)
print('ecg readings: ',e_list)
        

#AKIA6FZKI72YSM53M47Q,C8ncIojJ0sMA9kRa7muear+1DvJ1qr0hJRwqb1n7
#access key, secret key

 #   Access Key ID:
 #   AKIAIKXJLQKLM6WMD42Q
#    Secret Access Key:
 #   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


#upload temperture list to aws mysql

for i in t_list:
	sql = "INSERT INTO temperature (readings) VALUES(%s)"
	val = (int(i))
	mycursor.execute(sql,val)
	conn.commit()

#upload pulse list to aws mysql
for i in p_list:
	sql = "INSERT INTO pulse (readings) VALUES(%s)"
	val = (int(i))
	mycursor.execute(sql,val)
	conn.commit()

#upload ecg list to aws mysql
for i in e_list:
	sql = "INSERT INTO ECG (readings) VALUES(%s)"
	val = (int(i))
	mycursor.execute(sql,val)
	conn.commit()
