def exo6(n):
    s1,s2,S=0,0,0
    for i in range (1,n+1):
        s1+=i**2
        s2+=i
    s2=s2**2
    S=s2-s1
    return S


assert(exo6(10)==2640)
print(exo6(100))
