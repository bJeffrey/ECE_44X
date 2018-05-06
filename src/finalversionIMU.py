#! /usr/bin/env python
import rospy
import time
import serial

from std_msgs.msg import Empty
from math import pi
from std_msgs.msg import Float32

myvar= 1.38

#def callback(data):
#	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	#print data, "data captured before"
	#Possible float(data)
	
        #Joint
#	pub.publish(data)
        #Sensor
#	pub2.publish(data)
	#Pressure
#	pub3.publish(data)
	#Topics
#	pub4.publish(data)

#Gyro X Y Z
def GyroX(gyrox):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", gyrox.data)
	#pub = rospy.Publisher("RobotArm", Float32, queue_size=10)
	pub.publish(gyrox)

def GyroY(gyroy):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", gyroy.data)
	pub1.publish(gyroy)

def GyroZ(gyroz):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", gyroz.data)
	#pub = rospy.Publisher("RobotArm", Float32, queue_size=10)
	pub2.publish(gyroz)
#ACCELERATION X Y Z
def AccelX(accelx):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", accelx.data)
	#pub = rospy.Publisher("RobotArm", Float32, queue_size=10)
	pub3.publish(accelx)

def AccelY(accely):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", accely.data)
	pub4.publish(accely)

def AccelZ(accelz):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", accelz.data)
	#pub = rospy.Publisher("RobotArm", Float32, queue_size=10)
	pub5.publish(accelz)
#PRESSURE
def Pressure(pressure):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", pressure.data)
	#pub = rospy.Publisher("RobotArm", Float32, queue_size=10)
	pub6.publish(pressure)


if __name__ == "__main__":
	rospy.init_node("IMUNode")
	rospy.loginfo("IMU Node Online.")

	#Subscriber Stuff
	#sub = rospy.Subscriber('arduino', Float32, callback)
	sub = rospy.Subscriber('X_gyro', Float32, GyroX)
	sub1= rospy.Subscriber('Y_gyro', Float32, GyroY)
	sub2= rospy.Subscriber('Z_gyro', Float32, GyroZ)
	sub3 = rospy.Subscriber('X_accel', Float32, AccelX)
	sub4= rospy.Subscriber('Y_accel', Float32, AccelY)
	sub5= rospy.Subscriber('Z_accel', Float32, AccelZ)
	sub6= rospy.Subscriber('Pressure', Float32, Pressure)
	         
	#publisher 
	pub = rospy.Publisher('sssGyroX', Float32, queue_size=10)	
	pub1 = rospy.Publisher('sssGyroY', Float32, queue_size=10)
	pub2 = rospy.Publisher('sssGyroZ', Float32, queue_size=10)
	pub3 = rospy.Publisher('sssAccelX', Float32, queue_size=10)
	pub4 = rospy.Publisher('sssAccelY', Float32, queue_size=10)	
	pub5 = rospy.Publisher('sssAccelZ', Float32, queue_size=10)
	pub6 = rospy.Publisher('sssPressure', Float32, queue_size=10)
	
	
		
	
 	#pub3 = rospy.Publisher('drawer', Float32, queue_size=10)
	
	# Open the serial connection
	#ser = serial.Serial('/dev/ttyACM0', 9600)
	##ser = serial.Serial('/dev/ttyUSB0', 9600)
	##ser.readline()

	#Infinite Loop
        rospy.spin()

	#Decoding Values
	#while True:
		#vals = ser.readline().strip()
	        #print "Raw data '" + data + "'"
		#pub.publish(float(vals))

#		vals = vals.split(",")
#		print "Post split: ", vals
#		for idx, x in enumerate(vals):
#			vals[idx] = float(x)
#		delay(1000)
