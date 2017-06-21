import cPickle
import sys

if __name__ == '__main__':

	if(len(sys.argv) < 2):
		print 'invalid arguments, usage: <input.txt> <output.pickle>'
		exit()

	txtfilename = sys.argv[1]

	f = open(txtfilename,'r')
	worms = []

	saved = open(sys.argv[2],'w')
	for worm in f:
		worms.append(worm)
	cPickle.dump(worms,saved,cPickle.HIGHEST_PROTOCOL)

	saved.close()

	f.close()