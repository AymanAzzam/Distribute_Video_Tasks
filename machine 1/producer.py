import zmq 
import cv2
import numpy as np
import sys

host = "127.0.0.1"
port_out = 5557


def producer(video_directory) :
	
	capture = cv2.VideoCapture(video_directory)
	if (capture.isOpened() == False):
		print ("error opening the video file")
		return

	context = zmq.Context()
	zmq_socket_send = context.socket(zmq.PUSH)
	zmq_socket_send.bind("tcp://"+ host + ":%s" %port_out)

	frame_number=0
	print ("before entering the while looop")
	while(capture.isOpened() ) :
		ret, frame = capture.read()	
		if (ret == True):
			message = {'image': frame, 'framenumber': frame_number}
			zmq_socket_send.send_pyobj(message)
			print ("producer sent frame number %s" %frame_number)
			frame_number = frame_number+1
		else:
			break 

	capture.release()
	cv2.destroyAllWindows()	

producer(sys.argv[1])	
