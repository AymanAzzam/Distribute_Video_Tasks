import zmq
import sys

id1 = "127.0.0.1";  port1 = sys.argv[1]
id2 = "127.0.0.1";  port2 = sys.argv[2]

def producer():
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://%s:%s"%(id1,port1))

    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://%s:%s"%(id2,port2))

    while True:
        data = receiver.recv_pyobj()
        print("Collector1 Received Data")
        sender.send_pyobj(data)

producer()
