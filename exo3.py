def exo3(n):      
    s=0
    for i in range(1,n):
        if n%i==0 and premier(i):
            s=i
            n=n/i
    return s

#def exo3(n):      
    #s=0
    #i=n
    #while not(n%i==0 and premier(i)):
        #i-=1
    #s=i
    #return s
                
                
def premier(i):
    s=0
    n=int(i**(1/2))
    for j in range (2,n+1):
        if i%j==0: 
            return False
        else : s+=1
    if s==(n-1):
        return True
        
        
    #while (i%j!=0 and j**2<i):
        #j+=1  
    #if j==i:
        #return True
    #else : 
        #return False
        

assert (premier(11))
assert (exo3(13195)==29)
