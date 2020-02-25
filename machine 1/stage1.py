import zmq
import random
import matplotlib.pyplot as plt
import cv2 as cv
import sys





def consumer(port_in, port_out):
	
	my_id = random.randrange(10000)
	
	context = zmq.Context()
	consumer_reciever = context.socket(zmq.PULL)
	consumer_reciever.connect("tcp://127.0.0.1:%s" %port_in)

	consumer_sender = context.socket(zmq.PUSH)
	consumer_sender.connect("tcp://127.0.0.1:%s" %port_out)

	#print ("before entering the while looop")
	while True:
		recieved = consumer_reciever.recv_pyobj()
		print("consumer1_id %i recieved frame number %s" %(my_id,recieved['framenumber']))
		
		gray = cv.cvtColor(recieved['image'],cv.COLOR_BGR2GRAY)
		ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
		
		#gray = rgb2gray(recieved['image'])
		#thresh = threshold_otsu(gray)
		#binary = gray <= thresh
		#plt.imshow(binary)
		#plt.show()

		message= {'binaryimage':binary, 'framenumber': recieved['framenumber']}
		consumer_sender.send_pyobj(message)


consumer(int(sys.argv[1]), int(sys.argv[2]))  


