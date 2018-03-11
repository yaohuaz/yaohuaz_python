## How to run
	* $ python server.py
	* $ (open a new terminal)
	* $ python client.py

## Note
	* client sends 'Hello, world' to server
	* server appends '<from server>' after ther received message, and sends it back
	* client print `Received: '(received message)'`

## FAQ
	* socket.error: [Errno 48] Address already in use
		- port number is not closed. Need to wait for a while, and let system close the port number
		- how to fix: use XXX.close() after program
	* how to kill server.py
		- ctrl-c
