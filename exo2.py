def exo2(n):
    s=1
    i=0
    a=0
    Z=0
    while s<n:
        a=s
        s=s+i
        i=a
        if s%2==0: 
            Z+=s
    return Z

assert (exo2(8)==10)
print(exo2(4000000))


    

