	def prob_5	(l1, l2):
	wx=(l1[1]*l2[2]) - (l1[2]*l2[1])
	wy=(l1[2]*l2[0]) - (l1[0]*l2[2])
	wz=(l1[0]*l2[1]) - (l1[1]*l2[0])
	l3=[wx,wy,wz]
	return (l3)