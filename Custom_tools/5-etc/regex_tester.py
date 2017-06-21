import sys
import cPickle
import re

if __name__ == '__main__':

	if(len(sys.argv) < 2):
		print 'parameters: <file to check>'
		exit()
		
	#load signature
	file = open('signature.txt')
	regex = file.read()
	file.close()

	#load file to check
	file = open(sys.argv[1])
	traffics = cPickle.load(file)
	file.close()

	#check traffic
	for traffic in traffics:
		if(re.search(regex,traffic,re.M|re.I)):
			print 'success'
		else:
			print 'failed'