def premier(i):
    s=0
    n=int(i**(1/2))
    for j in range (2,n+1):
        if i%j==0: 
            return False
        else : s+=1
    if s==(n-1):
        return True

def exo10(n):
    s=0
    for i in range(2,n+1):
        if premier(i):
            s+=i
    return s

assert(exo10(10)==17)
print(exo10(2000000))

    