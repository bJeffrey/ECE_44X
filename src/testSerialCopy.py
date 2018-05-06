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
	port="/dev/ttyACM0" #This will be different for various devices and on windows it will probably be a COM port.
	print("before serial")	
	bluetooth = serial.Serial(port, 57600)#Start communications with the bluetooth unit
	print("Connected")
	#bluetooth.flushInput() #This gives the bluetooth a little kick

	rospy.init_node("imu_pressure")
	rospy.loginfo("IMU Pressure node online")
	xAccel = rospy.Publisher("X_accel", Float32, queue_size = 10)
	yAccel = rospy.Publisher("X_accel", Float32, queue_size = 10)
	zAccel = rospy.Publisher("X_accel", Float32, queue_size = 10)
	
	xGyro = rospy.Publisher("X_gyro", Float32, queue_size = 10)
	yGyro = rospy.Publisher("Y_gyro", Float32, queue_size = 10)
	zGyro = rospy.Publisher("Z_gyro", Float32, queue_size = 10)

	pressure = rospy.Publisher("Pressure", Float32, queue_size = 10)


	return bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure

#################################################################################
# Function:	publishIMU
# Description:	publishes IMU and pressure variables
#################################################################################
def publishIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure):
	xAccel.publish(float(data[1]))
	yAccel.publish(float(data[2]))
	zAccel.publish(float(data[3]))
	xGyro.publish(float(data[4]))
	yGyro.publish(float(data[5]))
	zGyro.publish(float(data[6]))
	pressure.publish(float(data[7]))
	
#################################################################################
# Function:	processData
# Description:	Identifies the source of the data and sends it to the function
#		to handle that source
#################################################################################
def processData(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure):

	if data[0] == "A":
		publishIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure)

#################################################################################
# Function:	main
# Description:	runs the loop to ingest data from the Arduinos
#################################################################################
def main(bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure):
	check = True
	loopCount = 0
	timeCheck = time.time()	

	while True: #send 5 groups of data to the bluetooth	
		input_data=bluetooth.readline().strip()#This reads the incoming data as a string
		
		if check == True:
			check = False
			t0 = time.time()

		
		data2 = input_data.split(" ")
		
		data = []
		for word1 in data2:
			word = word1.replace(" ", "")
			length = len(word)
			if length != 0:
				data.append(word) 
		print data		
		processData(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure)
		
		loopCount = loopCount + 1

		timeA = time.time()
		difference = timeA - timeCheck
		if difference >= 1:
			timeCheck = time.time()
			print "time since last check: ", difference
			print "Acceleration variables: ", loopCount * 3
			print "Gyroscopic variables: ", loopCount * 3
			print "Pressure variables: ", loopCount
			print ""
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
def exitCleanly(bluetooth):
	print '\nCTL^C received.  Exiting...'
	bluetooth.close()

if __name__ == "__main__":
	try:
		bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure = connect()
		main(bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro, pressure)
		#rospy.spin()
	except KeyboardInterrupt:
		exitCleanly(bluetooth)
