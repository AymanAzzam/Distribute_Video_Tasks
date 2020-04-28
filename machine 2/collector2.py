import zmq
import sys
import os

id = "127.0.0.1";  port = sys.argv[1]

if os.path.exists("output.txt"):
	os.remove("output.txt")

def producer():

    #print("collector_2 is created")

	context = zmq.Context()
	receiver = context.socket(zmq.PULL)
	receiver.bind("tcp://%s:%s"%(id,port))
	receiver.setsockopt(zmq.RCVTIMEO, 60000)

	while True:
		try :
			data = receiver.recv_pyobj()	
		except zmq.error.Again as e:
				#print('Alived rrrrece timed out ')
				break	
		print("collector2_id received frame number %s" %(data['framenumber']))
		
		#f.write("Frame Number %i \nContours: %i\n\n"%(data['framenumber'],5))
		################# trial code #######################
		f = open("output.txt","a")
		f.write("Frame Number %i \nContours: %s\n\n"%(data['framenumber'],len(data['contours'])))
		f.close()
		######################end trial#####################
		#f.write("Frame Number %i \nContours: %s\n\n"%(data['framenumber'],len(data['contours'])))
		#f.flush()

producer()

