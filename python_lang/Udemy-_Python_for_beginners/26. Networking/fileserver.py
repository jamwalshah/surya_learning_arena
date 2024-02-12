# fileserver.py
import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Server listening on port:", port)
s.listen(1)

c, addr = s.accept()
fileName = c.recv(1024) # receiving the filename from client
try:
    f = open(fileName, 'rb')
    content = f.read() # reading file that client requested
    c.send(content) # sending data from the requested file to the client
    f.close()
except FileNotFoundError:
    # print("File does not exist")
    c.send(b"File does not exist")

c.close()