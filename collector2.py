import zmq
import sys

id = "127.0.0.1";  port = sys.argv[1]

f = open("output.txt","w")

def producer():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://%s:%s"%(id,port))

    while True:
        data = receiver.recv_pyobj()
        print("Collector2 Received Data")
        f.write("Frame Number %i \nContours: %s\n\n"%(data['frame'],len(data['contours'])))

producer()
