import zmq
import cv2 as cv
import sys

id1 = "127.0.0.1";  port1 = sys.argv[1]
id2 = "127.0.0.1";  port2 = sys.argv[2]

def consumer():
    context = zmq.Context()
    
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://%s:%s"%(id1,port1))

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://%s:%s"%(id2,port2))
    
    while True:
        #Receive Data
        rec_data = receiver.recv_pyobj()
        print("Stage2 Received Data")
        if 'image' and 'frame' in rec_data:
            bin_img = rec_data['image']
            #Process Data
            major = cv.__version__.split('.')[0]
            if major == '3': img, bounding_boxes, hierarchy= cv.findContours(bin_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            else: bounding_boxes, hierarchy= cv.findContours(bin_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            #Send Data
            sent_data = {'frame':rec_data['frame'],'contours':bounding_boxes}
            sender.send_pyobj(sent_data)

        else:
            print("Process in Stage 2 Got Message without image or frame.")
        

consumer()