#tcpipclient.py
# to run these server & client snippets, run them with separate (jupyter/python) runtimes
import socket

s = socket.socket() # if parameters are passed, it takes Family=AF_INET and TypeOfConnection=socket.SOCK_STREAM
s.connect(("localhost", 4000)) # port 4000 becuse server is listening on port 4000

msg = s.recv(1024)
# print("DEBUG:",type(msg)) # debug
while msg:
    print("Received: ", msg.decode()) # decoding the message recieved in bytes to string
    # print("DEBUG:",type(msg.decode())) # debug
    msg = s.recv(1024)
s.close()