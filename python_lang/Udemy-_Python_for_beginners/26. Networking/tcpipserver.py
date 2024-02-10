# tcpipserver.py
# to run these server & client snippets, run them with separate (jupyter/python) runtimes
import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("DEBUG:",type(s)) # debug
# print("DEBUG:",s) #debug
s.bind((host, port))
# print("DEBUG:",s) # debug
print("Server listening on port:", port)
s.listen(1)
# print("DEBUG:",s) # debug
c, addr = s.accept()
# print("DEBUG:",type(c), type(addr)) # debug
print("Connection from:", str(addr))
c.send(b"Hello, how are you") # send data in byte string
c.send("bye".encode()) # encoding sting into bytes
# print("DEBUG:","bye".encode()) # debug
c.close()