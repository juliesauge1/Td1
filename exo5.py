def smallest(n):
    k=1
    a=2
    small=1
    for i in range (2,n):
        if premier(i):
            while i<=n :
                k=a
                a=a*k
                k+=1
                i=a
        small=small*i
    return small

def premier(i):
    s=0
    n=int(i**(1/2))
    for j in range (2,n+1):
        if i%j==0: 
            return False
        else : s+=1
    if s==(n-1):
        return True

        
        
        
        
       
       



        
        