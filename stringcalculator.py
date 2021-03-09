def add(s):
	if not s:
		return 0
	
	if ',' not in s:
		return int(s)

	return -1