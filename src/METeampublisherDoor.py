#! /usr/bin/env python
import rospy
import time
import serial

from std_msgs.msg import Empty
from math import pi
from std_msgs.msg import Float32

if __name__ == "__main__":
	#Node Online
	rospy.init_node("ME_Team_Door")
	rospy.loginfo("ME Door Team online.")
	
	#Publishers
        pub = rospy.Publisher('doorElec1', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub1 = rospy.Publisher('doorElec2', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub2 = rospy.Publisher('doorElec3', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub3 = rospy.Publisher('doorElec4', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub4 = rospy.Publisher('doorElec5', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub5 = rospy.Publisher('doorElec6', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub6 = rospy.Publisher('doorElec7', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub7 = rospy.Publisher('doorElec8', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub8 = rospy.Publisher('doorElec9', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub9 = rospy.Publisher('doorElec10', Float32, queue_size=10)# robotArmPressure,queue_size=10)
	pub10 = rospy.Publisher('doorElec11', Float32, queue_size=10)#robotArmSensor,queue_size=10)
	pub11 = rospy.Publisher('doorElec12', Float32, queue_size=10)#robotArmTopic,queue_size=10)

	pub12 = rospy.Publisher('doorResistance', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	pub13 = rospy.Publisher('doorForce', Float32, queue_size=10)#robotArmTopic,queue_size=10)
	
	# Open the serial connection
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser.readline()
	
	while True:
		#Get String from ME Drawer Team
		#Read Serial from connection above
		vals = ser.readline().strip()
		#Split that entire character array
		x = vals.split(',')

		#Elec1
		pub.publish(float(x[1]))
		#Elec2		
		pub1.publish(float(x[3]))
		#Elec3		
		pub2.publish(float(x[5]))
		#Elec4		
		pub3.publish(float(x[7]))
		#Elec5		
		pub4.publish(float(x[9]))
		#Elec6		
		pub5.publish(float(x[11]))
		#Elec7
		pub6.publish(float(x[13]))
		#Elec8
		pub7.publish(float(x[15]))
		#Elec9
		pub8.publish(float(x[17]))
		#Elec10
		pub9.publish(float(x[19]))
		#Elec11		
		pub10.publish(float(x[21]))
		#Elec12
		pub11.publish(float(x[23]))
		#Resistance
		pub12.publish(float(x[25]))
		#Force
		pub13.publish(float(x[27]))


