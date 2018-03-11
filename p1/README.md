## Python Practice 1

## Introduction 
Client Server Module 1. Simple client-server practice.

### Related Material && Package
	* socket 
	* json

### Requirements
	* two modules 
		- client 
		- server
	* server
		- running on localhost
		- port number: 5555
	* client 
		- send a json format request payload to server, and print out server returned answer payload info

### Request Payload Format
	data = {
		'operation' : '+ or - or * or /',
		'num_1' : #1 value,
		'num_2'	: #2 value
	}	
### Answer Payload Format
	data = {
		'Error Message': '',
		'Answer': ''
	}

If `Error Message` is empty, print out `Answer`; otherwise, print out `Error Message` 

### Hint
1. client-server
	- read files `client-server` ppt. Study basic client-server and socket ideas

2. socket client server module.
	- use `client-server` ppt example code, or online resourse to build a simple echo back client-server module

3. json
	- seach `json python` related things online

