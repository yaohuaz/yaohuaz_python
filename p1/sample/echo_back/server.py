import socket
#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to localhost, and port number: 5000
serversocket.bind(('localhost', 5000))

# become a server socket 5
serversocket.listen(5)

print ('Server established..')
try:
    while True:
        #accept connections from outside
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024)
        if not data: 
            break
        clientsocket.send(data + '  <from server>') 
        clientsocket.close()
except:
    serversocket.close()
