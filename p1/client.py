import socket
import json

num_1= input('enter first value: ')
num_2= input('enter second value: ')
data = dict({"operation" : "+ or - or * or /","num_1" : num_1, "num_2" : num_2})
data1 = json.dumps(data, indent=2)

HOST = 'localhost'    # The remote host
PORT = 5555              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(data1)

data3 = s.recv(1024)
info = json.loads(data3)
if len(info['Error message']) >0:
    print(info['Error message'])
else:
    del info['Error message']
    print 'Received:', repr(info)
