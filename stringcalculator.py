def add(s):
	if not s:
		return 0
	
	if ',' not in s:
		return int(s)
	else:
		a = s.split(',')
		return int(a[0]) + int(a[1])

	return -1