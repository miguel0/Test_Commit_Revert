def add(s):
	if not s:
		return 0
	
	delimiter = ','
	if not s[0].isdigit():
		if s[1] == '\n':
			delimiter = s[0]
			s = s[2:]
		else:
			raise TypeError('bad delimiter formatting')
	else:
		s = s.replace('\n', ',')

	return sum([int(x) for x in s.split(delimiter)])