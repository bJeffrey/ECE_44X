#! /usr/bin/env python
#import rospy
import serial
import time

#from std_msgs.msg import Float32


def connect():
	print("Start")
	port="/dev/rfcomm0" #This will be different for various devices and on windows it will probably be a COM port.
	bluetooth=serial.Serial(port, 115200)#Start communications with the bluetooth unit
	print("Connected")
	bluetooth.flushInput() #This gives the bluetooth a little kick

#	rospy.init_node("imu_pressure")
#	rospy.loginfo("IMU Pressure node online")
#	xAccel = rospy.publisher("X_accel", Float32, queue_size = 10)
	xAccel = 0
	return bluetooth, xAccel

def processData(data, xAccel):

	if data[0] == "Accell":
		xAccel.publish(float(data[1]))
		

def main(bluetooth, xAccel):
	check = True
	for i in range(10): #send 5 groups of data to the bluetooth	
		input_data=bluetooth.readline().strip()#This reads the incoming data as a string
		
		if check == True:
			check = False
			t0 = time.time()
		
		print 'Iteration', i

		
		data2 = input_data.split(" ")
		
		x = 0
		data = []
		for word1 in data2:
			#word = data1.replace(" ", "")
			word = word1.replace(" ", "")
			length = len(word)
			if length != 0:
				data.append(word) 
				#print word2, "Length: ", length
		print data		
		#processData(data, xAccel)
		

	t1 = time.time()
	total = t1 - t0
	print 'Total time: ', total
	bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/rfcommX
	print("Done")

def exitCleanly(bluetooth):
	print '\nCTL^C received.  Exiting...'
	bluetooth.close()

if __name__ == "__main__":
	try:
		bluetooth, xAccel = connect()
		main(bluetooth, xAccel)
	except KeyboardInterrupt:
		exitCleanly(bluetooth)
