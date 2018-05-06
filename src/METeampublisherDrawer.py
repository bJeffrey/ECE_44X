#! /usr/bin/env python
import rospy
import time
import serial

from std_msgs.msg import Empty
from math import pi
from std_msgs.msg import Float32

if __name__ == "__main__":
	#Node Online
	rospy.init_node("ME_Drawer_Team")
	rospy.loginfo("ME Drawer Team online.")
	
	timeStart = time.time()

	#Publishers
        pub = rospy.Publisher('drawerTime', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub1= rospy.Publisher('drawerPosition', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub2= rospy.Publisher('drawerVelocity', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub3 = rospy.Publisher('drawerAcceleration', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub4= rospy.Publisher('drawerFSR1', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub5= rospy.Publisher('drawerFSR2', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub6= rospy.Publisher('drawerFSR3', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub7= rospy.Publisher('drawerFSR4', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub8= rospy.Publisher('drawerFSRSum', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	
	# Open the serial connection
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser.readline()
	
	while True:
		#Get String from ME Drawer Team
		#Read Serial from connection above
		vals = ser.readline().strip()
		#Split that entire character array
		x = vals.split(',')

		#Time
		pub.publish(float(x[1]))
		#Position		
		pub1.publish(float(x[3]))
		#Veocity		
		pub2.publish(float(x[5]))
		#Acceleration		
		pub3.publish(float(x[7]))
		#FSR1		
		pub4.publish(float(x[9]))
		#FSR2		
		pub5.publish(float(x[11]))
		#FSR3
		pub6.publish(float(x[13]))
		#FSR4
		pub7.publish(float(x[15]))
		#FSR Sum
		pub8.publish(float(x[17]))
		
		##print "One Cycle";		
		#timeEnd = time.time()
        	#totalTime = timeEnd - timeStart
		#print totalTime;


