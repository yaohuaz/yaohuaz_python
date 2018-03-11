import socket
import json
#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to localhost, and port number: 5000
serversocket.bind(('localhost', 5555))

# become a server socket 5
serversocket.listen(5)

print ('Server established..')
try:
    while True:
        #accept connections from outside

        (clientsocket, address) = serversocket.accept()
        js = clientsocket.recv(1024)
        data = json.loads(js)
        if not data:
            break

        try:
            x1 = float(data["num_1"])
            x2 = float(data["num_2"])
            tot = x1 + x2
            diff = x1 - x2
            prod = x1 * x2
            quot = x1 / x2
            msg = ''
        except:
            tot =''
            diff = ''
            prod = ''
            quot = ''
            msg = 'input value is not a number'
        data2 = dict({'Error message':msg, 'sum': tot, 'difference': diff, 'product': prod, 'quotient': quot})
        data3 = json.dumps(data2, indent=2)
        print(data3)
        clientsocket.send(data3)
        clientsocket.close()


except:
            print('not received')
            serversocket.close()
