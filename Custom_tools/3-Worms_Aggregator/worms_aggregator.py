import re
import os
import cPickle

if __name__ == '__main__':
	path = 'log/'

	worms = []

	for logfilename in os.listdir(path):
		f = open(path + logfilename,'r')
		
		#regex for traffic in log
		pattern = r"\('in', b'(.+)'\)"
		matchObj = re.search(pattern,f.read())

		#delete one \x0d0a if double in last line(some bugs in polygraph signature generator if 2)
		sample = matchObj.group(1)
		if(sample[-16:].lower() == '\\x0d\\x0a\\x0d\\x0a'.lower()):
			sample = sample[:-8]
		sample = sample.decode('string-escape')

		worms.append(sample)
		f.close()

	#write worm to worm pickle file
	wormPickle = open('worm.pickle', 'w')
	cPickle.dump(worms,wormPickle,cPickle.HIGHEST_PROTOCOL)
	wormPickle.close()