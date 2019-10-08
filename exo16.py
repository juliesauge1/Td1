def exo16(n):
    a=2**n
    a=str(a)
    s=0
    l=len(a)
    for i in range(0,l):
        b=a[i]
        b=int(b)
        s+=b
    return s

assert(exo16(15)==26)
print(exo16(1000))



