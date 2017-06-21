import cPickle
import sys

if __name__ == '__main__':

	if(len(sys.argv) < 2):
		print 'invalid arguments, usage: <input.pickle> <output.txt>'
		exit()

	logfilename = sys.argv[1]

	f = open(logfilename,'r')
	worms = cPickle.load(f)
	f.close()

	saved = open(sys.argv[2],'w')
	for worm in worms:
		saved.write(worm)
	saved.close()
