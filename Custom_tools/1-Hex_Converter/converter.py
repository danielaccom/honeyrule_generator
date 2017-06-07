if __name__ == '__main__':
	a = open('log.txt')
	strings = a.read().splitlines()

	b = open('log-out.txt','w')
	for s in strings:
		b.write(s.decode('string-escape'))

	a.close()
	b.close()
