import zmq
import random
import matplotlib.pyplot as plt
import cv2
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import sys

host = "127.0.0.1"



def consumer(portin, portout) :

	port_in = portin
	port_out = portout

	context = zmq.Context()
	consumer_reciever = context.socket(zmq.PULL)
	consumer_reciever.connect("tcp://"+ host + ":%s" %port_in)
	
	consumer_sender = context.socket(zmq.PUSH)
	consumer_sender.connect("tcp://"+ host + ":%s" %port_out)

	print ("before entering the while looop")
	while True:
		recieved = consumer_reciever.recv_pyobj()
		gray = rgb2gray(recieved['image'])
		thresh = threshold_otsu(gray)
		binary = gray <= thresh
		plt.imshow(binary)
		plt.show()
		print("consumer recieved frame number %s" %recieved['framenumber'])

		message= {'binaryimage':binary, 'framenumber': recieved['framenumber']}
		consumer_sender.send_pyobj(message)


consumer(int(sys.argv[1]), int(sys.argv[2]))  		

