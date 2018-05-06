#! /usr/bin/env python
import rospy
import serial
import time

from std_msgs.msg import Float32

################################################################################
# Function:	connect
# Description:	initializes serial connection and topics
################################################################################
def connect():
	print("Start")
	port="/dev/rfcomm0" #This will be different for various devices and on windows it will probably be a COM port.
	print("before serial")
	#bluetooth = None
	#pressureSerial = None
	try:
		bluetooth = serial.Serial(port, 115200)#Start communications with the bluetooth unit
		print("Connected to bluetooth")
		#bluetooth.flushInput() #This gives the bluetooth a little kick
		#bluetooth = None
	except serial.serialutil.SerialException:
		print("Failed to connect to Bluetooth")
		bluetooth = None


	try:
		pressureSerial = serial.Serial("/dev/ttyACM0", 115200)
		print("Connected to pressure sensor serial port")
	except serial.serialutil.SerialException:
		print("Failed to connect to pressure sensor serial port")
		pressureSerial = None

	rospy.init_node("imu_pressure")
	rospy.loginfo("IMU Pressure node online")

	xAccel = rospy.Publisher("X_accel", Float32, queue_size = 10)
	yAccel = rospy.Publisher("Y_accel", Float32, queue_size = 10)
	zAccel = rospy.Publisher("Z_accel", Float32, queue_size = 10)
	
	xGyro = rospy.Publisher("X_gyro", Float32, queue_size = 10)
	yGyro = rospy.Publisher("Y_gyro", Float32, queue_size = 10)
	zGyro = rospy.Publisher("Z_gyro", Float32, queue_size = 10)

	press1 = rospy.Publisher("Press1", Float32, queue_size = 10)
	press2 = rospy.Publisher("Press2", Float32, queue_size = 10)
	press3 = rospy.Publisher("Press3", Float32, queue_size = 10)
	press4 = rospy.Publisher("Press4", Float32, queue_size = 10)
	press5 = rospy.Publisher("Press5", Float32, queue_size = 10)
	press6 = rospy.Publisher("Press6", Float32, queue_size = 10)
	press7 = rospy.Publisher("Press7", Float32, queue_size = 10)
	press8 = rospy.Publisher("Press8", Float32, queue_size = 10)
	press9 = rospy.Publisher("Press9", Float32, queue_size = 10)
	press10 = rospy.Publisher("Press10", Float32, queue_size = 10)
	press11 = rospy.Publisher("Press11", Float32, queue_size = 10)
	press12 = rospy.Publisher("Press12", Float32, queue_size = 10)


	pressure = rospy.Publisher("Pressure", Float32, queue_size = 10)


	return bluetooth, pressureSerial, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12, pressure

#################################################################################
# Function:	publishIMU
# Description:	publishes IMU and pressure variables
#################################################################################
def publishIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro):
#	pass
	#print data
	#absValue = float(data[4]) * float(data[4]) + float(data[5]) * float(data[5]) + float(data[6]) * float(data[6]) 
	#absValue = absValue ** (1/2.0)
	#if data[0] == "IMU":

	try:
		xAccel.publish(float(data[1]))
	except ValueError:
		print ("Error reading x acceleration")
	except IndexError:
		print("Index error on x acceleration")
	try:
		yAccel.publish(float(data[2]))
	except ValueError:
		print ("Error reading y acceleration")
	except IndexError:
		print("Index error on y acceleration")
	try:
		zAccel.publish(float(data[3]))
	except ValueError:
		print ("Error reading z acceleration")
	except IndexError:
		print("Index error on z acceleration")
	try:
		xGyro.publish(float(data[4]))
	except ValueError:
		print ("Error reading x gyro")
	except IndexError:
		print("Index error on x gyro")
	try:
		yGyro.publish(float(data[5]))
	except ValueError:
		print ("Error reading y gyro")
	except IndexError:
		print("Index error on y gyro")
	try:
		zGyro.publish(float(data[6]))
	except ValueError:
		print ("Error reading z gyro")
	except IndexError:
		print("Index error on z gyro")


#################################################################################
# Function:	processIMU
# Description:	Identifies the source of the data and sends it to the function
#		to handle that source
#################################################################################
def processIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro):
		publishIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro)

#################################################################################
# Function:	processPressure
# Description:	Identifies the source of the data and sends it to the function
#		to handle that source
#################################################################################
def processPressure(pressureData, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12):

	try:
		float(pressureData[0])
		press1.publish(float(pressureData[0]))
	except ValueError:
		print ("Error reading pressure 1")
	except IndexError:
		print("Index error on pressure 1")
	try:
		float(pressureData[1])
		press2.publish(float(pressureData[1]))
	except ValueError:
		print ("Error reading pressure 2")
	except IndexError:
		print("Index error on pressure 2")
	try:
		float(pressureData[2])
		press3.publish(float(pressureData[2]))
	except ValueError:
		print ("Error reading pressure 3")
	except IndexError:
		print("Index error on pressure 3")
	try:
		float(pressureData[3])
		press4.publish(float(pressureData[3]))
	except ValueError:
		print ("Error reading pressure 4")
	except IndexError:
		print("Index error on pressure 4")	
	try:
		float(pressureData[4])
		press5.publish(float(pressureData[4]))
	except ValueError:
		print ("Error reading pressure 5")
	except IndexError:
		print("Index error on pressure 5")
	try:
		float(pressureData[5])
		press6.publish(float(pressureData[5]))
	except ValueError:
		print ("Error reading pressure 6")
	except IndexError:
		print("Index error on pressure 6")
	try:
		float(pressureData[6])
		press7.publish(float(pressureData[6]))
	except ValueError:
		print ("Error reading pressure 7")
	except IndexError:
		print("Index error on pressure 7")
	try:
		float(pressureData[7])
		press8.publish(float(pressureData[7]))
	except ValueError:
		print ("Error reading pressure 8")
	except IndexError:
		print("Index error on pressure 8")
	try:
		float(pressureData[8])
		press9.publish(float(pressureData[8]))
	except ValueError:
		print ("Error reading pressure 9")
	except IndexError:
		print("Index error on pressure 9")
	try:
		float(pressureData[9])
		press10.publish(float(pressureData[9]))
	except ValueError:
		print ("Error reading pressure 10")
	except IndexError:
		print("Index error on pressure 10")
	try:
		float(pressureData[10])
		press11.publish(float(pressureData[10]))
	except ValueError:
		print ("Error reading pressure 11")
	except IndexError:
		print("Index error on pressure 11")
	try:
		float(pressureData[11])
		press12.publish(float(pressureData[11]))
	except ValueError:
		print ("Error reading pressure 12")
	except IndexError:
		print("Index error on pressure 12")


#################################################################################
# Function:	main
# Description:	runs the loop to ingest data from the Arduinos
#################################################################################
def main(bluetooth, pressureSerial, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12, pressure):

	check = checkPressure = checkBT = True
	loopCount = pressureCount = BTReceiveCount = 0
	timeCheck = pressTimeCheck = time.time()	

	while True: #send 5 groups of data to the bluetooth

		if bluetooth != None:	
			input_data=bluetooth.readline().strip()#This reads the incoming data as a string
			print input_data

			data2 = input_data.split(",")
			data = []
			for word1 in data2:
				word = word1.replace(" ", "")
				length = len(word)
				if length != 0:
					data.append(word) 
			#print data		
			processIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro)

		if pressureSerial != None:
			readPressure = pressureSerial.readline().strip()
			print (readPressure)
			#readPressure = pressureSerial.read(56).strip()

			if checkPressure == True:
				checkPressure = False
				t0Pressure = time.time()

			pressureCount = pressureCount + 1
			pressureTime = time.time()
			pressTimeDiff = pressureTime - pressTimeCheck
			if pressTimeDiff >= 1:
				pressTimeCheck = time.time()
				#print "It's been 1 second.  Read ", pressureCount * 12, " pressure variables"
				pressureCount = 0
				#print ""

			splitData = readPressure.split(",")
			pressureData = []
			for word1 in splitData:
				word = word1.replace(" ", "")
				length = len(word)
				if length != 0:
					pressureData.append(word) 
			#print pressureData
			processPressure(pressureData, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12)
				

		if check == True:
			check = False
			t0 = time.time()
		
		loopCount = loopCount + 1

		timeA = time.time()
		difference = timeA - timeCheck
		if difference >= 1:
			timeCheck = time.time()
			#print "time since last check: ", difference
			#print "Acceleration variables: ", loopCount * 3
			#print "Gyroscopic variables: ", loopCount * 3
			#print "Pressure variables: ", loopCount
			#print ""
			loopCount = 0



	t1 = time.time()
	total = t1 - t0
	print 'Total time: ', total
	bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/rfcommX
	print("Done")

#################################################################################
# Function:	exitCleanly
# Description:	close the serial interface
#################################################################################
def exitCleanly(bluetooth, pressureSerial):
	print '\nCTL^C received.  Exiting...'
	bluetooth.close()
	pressureSerial.close()

if __name__ == "__main__":
	try:
		bluetooth, pressureSerial, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12, pressure = connect()
		main(bluetooth, pressureSerial, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12, pressure)
		#rospy.spin()
	except KeyboardInterrupt:
		exitCleanly(bluetooth, pressureSerial)
