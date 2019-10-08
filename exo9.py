def exo9(n):
	for i in range(1,n):
		for j in range(i+1,n):
			k=n-i-j
			if i**2+j**2==k**2:
				p=i*j*k
	
	return p


assert(exo9(12)==60)
print(exo9(1000))
