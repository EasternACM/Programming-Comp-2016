pre = "../data/secret/"
post = ".in"
def mastermind(fname):
	with open(fname) as r:
		l = r.readline()
		t = l.split()
	n = int(t[0])
	code = t[1]
	guess = t[2]

	r_list = [] #identical in color and position
	for i in xrange(0, n):
		if code[i] == guess[i]:
			r_list.append(code[i])
	r = len(r_list)
	#todo repeats in code can count for both s and r. How to hangle? Need each element to be unique, I think. Replace each letter with an integer congruent with it's letter, but non repeating in the set?
	s = len((set(guess)) & set(code) - set(r_list)) #identical in color but NOT position (& is intersection)
	return str(r) + " " + str(s)

#file loop
start = 5
end = 55
for i in xrange(start, end+1):
	num = ('%0*d' %  (3, i)) #pad number with zeros
	fname = pre + num + post 
	val = mastermind(fname)
	print(num + ": " + val)