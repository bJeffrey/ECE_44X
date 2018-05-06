#! /usr/bin/env python
#################################################################################
# Program: IMU.py
# Author: Jeffrey Noe
#################################################################################

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
	bluetooth = None
	try:
		bluetooth = serial.Serial(port, 115200)#Start communications with the bluetooth unit
		print("Connected to bluetooth")
		#bluetooth.flushInput() #This gives the bluetooth a little kick
		#bluetooth = None
	except serial.serialutil.SerialException:
		print("Failed to connect to Bluetooth")
		bluetooth = None

	rospy.init_node("IMU")
	rospy.loginfo("IMU node online")

	xAccel = rospy.Publisher("X_accel", Float32, queue_size = 10)
	yAccel = rospy.Publisher("Y_accel", Float32, queue_size = 10)
	zAccel = rospy.Publisher("Z_accel", Float32, queue_size = 10)
	
	xGyro = rospy.Publisher("X_gyro", Float32, queue_size = 10)
	yGyro = rospy.Publisher("Y_gyro", Float32, queue_size = 10)
	zGyro = rospy.Publisher("Z_gyro", Float32, queue_size = 10)

	return bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro

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
# Function:	main
# Description:	runs the loop to ingest data from the Arduinos
#################################################################################
def main(bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro):

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
			publishIMU(data, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro)

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
def exitCleanly(bluetooth):
	print '\nCTL^C received.  Exiting...'
	bluetooth.close()

if __name__ == "__main__":
	try:
		bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro = connect()
		main(bluetooth, xAccel, yAccel, zAccel, xGyro, yGyro, zGyro)
		#rospy.spin()
	except KeyboardInterrupt:
		exitCleanly(bluetooth)
