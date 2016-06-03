def prob_9 (l1):
	l1.sort()
	res=((l1[0]**2) + (l1[1]**2))
	if res== l1[2]**2:
		return True
	else:
		return False