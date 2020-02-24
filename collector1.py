import zmq
import sys
import random

id1 = "127.0.0.1";  port1 = sys.argv[1]
id2 = sys.argv[3];  port2 = sys.argv[2]

def producer():

    my_id = random.randrange(10000)
    #print("collector_1 id number ",my_id," is created")
    
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://%s:%s"%(id1,port1))

    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://%s:%s"%(id2,port2))

    while True:
        data = receiver.recv_pyobj()
        print("collector1_id %i received frame number %s" %(my_id, data['framenumber']))
        sender.send_pyobj(data)

producer()
