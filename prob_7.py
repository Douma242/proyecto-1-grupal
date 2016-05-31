def prob_7(l1):
	miset=[4, 7]
	n=1
	res=0
	while res<1000:
		n=n+1
		res=miset[0]*n
		miset.append(res)
	n2=1
	res2=0
	while res2<994:
		n2=n2+1
		res2=miset[1]*n2
		miset.append(res2)
	miset.sort()
	return miset