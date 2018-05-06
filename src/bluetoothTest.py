#! /usr/bin/env python
import serial
import time

def connect():
	print("Start")
	port="/dev/ttyUSB0" 
	rate = 9600
	ser = serial.Serial(port, rate, timeout = None, xonxoff = False, rtscts = False, dsrdtr = False)
	print("Connected")
	ser.flushInput()
	ser.flushOutput()
	return ser

def main(ser):
	check = True
	for i in range(10): #send 5 groups of data to the bluetooth
			
		#bytesToRead=ser.inWaiting()#This reads the incoming data as a string
		input_data = ser.readline().strip()
#		print input_data
		if check == True:
			check = False
			t0 = time.time()
		
		
		data = input_data.split(" ")
		for word in data:
			print word
			length = len(word)
			print "Length", length


#			#print t0
#		print 'Iteration', i
		
		
#		x = 0
#		for y in input_data:
#			data = input_data[x]
			#print (data)
			#print (type(data))
#			if data == ' ':
#				print ("I found one")
#			x = x + 1

	t1 = time.time()
	total = t1 - t0
	print 'Total time: ', total
		
	ser.close() 

	print("Done")

def exitCleanly(ser):
	print '\nCTL^C received.  Exiting...'
	ser.close()

if __name__ == "__main__":
	try:
		ser = connect()
		main(ser)
	except KeyboardInterrupt:
		exitCleanly(ser)
