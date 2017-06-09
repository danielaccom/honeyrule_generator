import cPickle
import os

if __name__ == '__main__':
	for logfilename in os.listdir('.'):
		if(logfilename.find('.pickle') != -1):
			f = open(logfilename,'r')
			worms = cPickle.load(f)
			
			#sort and limit to 100
			#worms = worms[:100]
			#worms.sort()

			f.close()

			saved = open(logfilename[:-7] + '.txt','w')
			for worm in worms:
				saved.write(worm)
			saved.close()
