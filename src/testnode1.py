#! /usr/bin/env python
import rospy
import time
import serial

#import std_msgs

from std_msgs.msg import Empty
from math import pi
#from std_msgs.msg import Int32
from std_msgs.msg import Float32

if __name__ == "__main__":
	rospy.init_node("bhand_sliders")
	rospy.loginfo("Everything is working properly so far!")
	
	#'arduino' is the topic being published
	pub=rospy.Publisher('arduino', Float32, queue_size=10)
	
	# Open the serial connection
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser.readline()
	
	while True:
		vals = ser.readline().strip()
		print "Raw data '" + vals + "'"
		pub.publish(float(vals))
