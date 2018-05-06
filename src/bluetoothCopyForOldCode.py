#! /usr/bin/env python
import serial
import time

def connect():
	print("Start")
	port="/dev/rfcomm0" #This will be different for various devices and on windows it will probably be a COM port.
	bluetooth=serial.Serial(port, 115200)#Start communications with the bluetooth unit
	print("Connected")
	bluetooth.flushInput() #This gives the bluetooth a little kick
	return bluetooth
def main(bluetooth):
	check = True
	for i in range(10): #send 5 groups of data to the bluetooth
	#	print("Ping")
	#	bluetooth.write(b"BOOP "+str.encode(str(i)))#These need to be bytes not unicode, plus a number		
		input_data=bluetooth.readline()#This reads the incoming data as a string
		if check == True:
			check = False
			t0 = time.time()
			#print t0
		print 'Iteration', i
		#data = input_data.decode()
		#data.encode('ascii', 'ignore')
		#print (type(input_data))
		#print (input_data)
		data = input_data.split(" ")
		for word in data:
			length = len(word)
			print word, "Length: ", length

		x = 0
		for y in input_data:
			data = input_data[x]
			#print (data)
			#print (type(data))
			#if data == ' ':
			#	print ("I found one")
			x = x + 1

	t1 = time.time()
	total = t1 - t0
	print 'Total time: ', total
		#print(input_data.decode())#These are bytes coming in so a decode is needed
		#time.sleep(0.01) #A pause between bursts
	bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/rfcommX

	print("Done")

def exitCleanly(bluetooth):
	print '\nCTL^C received.  Exiting...'
	bluetooth.close()

if __name__ == "__main__":
	try:
		bluetooth = connect()
		main(bluetooth)
	except KeyboardInterrupt:
		exitCleanly(bluetooth)
