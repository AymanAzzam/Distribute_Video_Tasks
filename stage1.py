import zmq
import random
import matplotlib.pyplot as plt
import cv2
from skimage.filters import threshold_otsu

host = "127.0.0.1"
port_in = 5557
port_out = 5558


def consumer() :

	context = zmq.Context()
	consumer_reciever = context.socket(zmq.PULL)
	consumer_reciever.connect("tcp://"+ host + ":%s" %port_in)
	
	consumer_sender = context.socket(zmq.PUSH)
	consumer_sender.connect("tcp://"+ host + ":%s" %port_out)

	print ("before entering the while looop")
	while True:
		recieved = consumer_reciever.recv_pyobj()
		thresh = threshold_otsu(recieved['image'])
		binary = recieved['image'] <= thresh
		
		print("consumer recieved frame number %s" %recieved['framenumber'])


consumer()  		


