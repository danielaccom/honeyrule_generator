import pickle
import socket
import sys
import random

if __name__ == '__main__':

	if(len(sys.argv) < 3):
		print 'usage: argument 1 = worm pickle file, argument 2 = ip destination, argument 3 port destination'
		exit()

	f = open(sys.argv[1])
	remote_ip = sys.argv[2]
	port = int(sys.argv[3])
	
	worms = pickle.load(f)
	random.shuffle(worms)

	#truncate if > 100
	if(len(worms) > 100):
		worm_counts = 100
	else:
		worm_counts = len(worms)
	
	success = 0

	for i in range(0,worm_counts):
		print '####attempt %d####' % (i+1)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((remote_ip, port))
	
			#message = 'GET / HTTP/1.1\r\nHost: 192.168.149.142\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nIf-Modified-Since: Fri, 18 Jul 2014 03:03:36 GMT\r\nIf-None-Match: "e036a-b1-4fe6f00e4242a"\r\nCache-Control: max-age=0\r\n\r\n'
			#message = 'GET / HTTP/1.1\r\n\r\n'
			
			message = worms[i] + '\r\n'
			s.sendall(message)
	
			reply = s.recv(4096)
	
			print(reply)
			s.close()
			success += 1
		except socket.error, e:
			print e

	print '%d success' % success