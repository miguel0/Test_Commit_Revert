def add(s):
	if not s:
		return 0
	
	delimiter = ','
	if not s[0].isdigit():
		if s[1] == '\n':
			delimiter = s[0]
			s = s[2:]
		else:
			if s[0] != '-':
				raise TypeError('bad delimiter formatting')
	else:
		s = s.replace('\n', ',')
	
	nums = [int(x) for x in s.split(delimiter)]

	if min(nums) < 0:
		negatives = [x for x in nums if x < 0]
		neg_str = ', '.join(negatives)
		raise TypeError('negatives not allowed: ' + neg_str)

	return sum(nums)