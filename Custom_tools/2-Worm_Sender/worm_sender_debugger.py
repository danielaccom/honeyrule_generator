import pickle
import socket
import sys
import random

if __name__ == '__main__':

	if(len(sys.argv) < 2):
		print 'usage: argument 1 = ip, argument 2 = port'
		exit()

	f = open("apache.pickle")
	worms = pickle.load(f)
	random.shuffle(worms)

	remote_ip = sys.argv[1]
	port = int(sys.argv[2])
	
	success = 0
	attempts = len(worms)
	print attempts

	failed = open('failed.txt','w')
	successed = open('success.txt','w')
	for i in range(0,8):
		successed.write(worms[i])
	successed.close()

	for i in range(0,attempts):
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
			failed.write(worms[i])
		except socket.error, e:
			print e

	print '%d success' % success
	failed.close()