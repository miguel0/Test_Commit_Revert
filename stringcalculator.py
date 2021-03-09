def add(s):
	if not s:
		return 0
	
	s = s.replace('\n', ',')
	return sum([int(x) for x in s.split(',')])