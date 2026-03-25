def duf(q):
	cpunt=0	
	for ch in q:
		if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			cpunt  =cpunt+1
	return cpunt
	
print(duf('PYthonPrOG')) 
		
#output 5