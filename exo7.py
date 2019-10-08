def premier(i):
    s=0
    n=int(i**(1/2))
    for j in range (2,n+1):
        if i%j==0: 
            return False
        else : s+=1
    if s==(n-1):
        return True

def exo7(n):
    i=2
    s=0
    while s<n:
        if premier(i):
            s+=1
            i+=1
        else:
            i+=1
    return i-1 


assert(exo7(6)==13)
print(exo7(10001))



