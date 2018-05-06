#! /usr/bin/env python
#################################################################################
# Program: pressure.py
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
	port = "/dev/ttyACM0"
	rate = 115200
	try:
		pressureSerial = serial.Serial(port, rate)
		print("Connected to pressure sensor serial port")
	except serial.serialutil.SerialException:
		print("Failed to connect to pressure sensor serial port")
		pressureSerial = None

	rospy.init_node("Pressure")
	rospy.loginfo("Pressure node online")

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

	return pressureSerial, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12

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
def main(pressureSerial, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12):

	check = checkPressure = checkBT = True
	loopCount = pressureCount = BTReceiveCount = 0
	timeCheck = pressTimeCheck = time.time()	

	while True: #send 5 groups of data to the bluetooth
		if pressureSerial != None:
			readPressure = pressureSerial.readline().strip()
			#print (readPressure)

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
			print pressureData
			processPressure(pressureData, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12)
				

		if check == True:
			check = False
			t0 = time.time()
		
		loopCount = loopCount + 1

		timeA = time.time()
		difference = timeA - timeCheck
		if difference >= 1:
			timeCheck = time.time()
			#print "Pressure variables per second: ", loopCount * 12
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
def exitCleanly(pressureSerial):
	print '\nCTL^C received.  Exiting...'
	pressureSerial.close()

if __name__ == "__main__":
	try:
		pressureSerial, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12 = connect()
		main(pressureSerial, press1, press2, press3, press4, press5, press6, press7, press8, press9, press10, press11, press12)
		#rospy.spin()
	except KeyboardInterrupt:
		exitCleanly(pressureSerial)
