import cPickle

if __name__ == '__main__':

	f = open("apache.pickle")
	worms = cPickle.load(f)
	worms = worms[:20]
	f.close()

	f = open("apache.pickle", 'w')
	cPickle.dump(worms, f, cPickle.HIGHEST_PROTOCOL)
	f.close()