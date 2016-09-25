
pre = "../data/secret/"
post = '.in'
def bottle_up(fname, num):
	with open(fname) as r:
		l = r.readline()
		s = l.split()
	oil = int(s[0])
	bigV = int(s[1])
	smlV = int(s[2])

	impossibleFlag = False

	bigN = 0
	smalN = 0
	try: #if data is bad
		if oil % bigV == 0:
			bigN = oil // bigV
			smlN = 0
		else:
			bigN = oil // bigV
			attempt = oil % bigV
			while attempt % smlV != 0:
				attempt += bigV
				bigN -= 1
				if bigN < 0 or oil < attempt:
					impossibleFlag = True
					break
			smlN = attempt // smlV
	except:
		impossibleFlag = True
	if impossibleFlag:
		return (num + ": Impossible")
	else:
		return (num + ": " + str(bigN) + " " + str(smlN))

#file loop
for i in xrange(4, 43):
	num = ('%0*d' %  (3, i)) #pad number with zeros
	fname = pre + num + post 
	val = bottle_up(fname, num)
	print val