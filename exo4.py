def plusgros(n):
    inf=10**(n-1)
    sup=10**n
    L=[]
    for i in range(inf,sup):
        for j in range(inf,sup):
            if palindrome(i*j):
                p=i*j
                L.append(p)
    m=max(L)
    return m

def palindrome(n):
    n=str(n)
    l=len(n)
    if l%2==0:
        r=int(l/2)
        s=0
        for i in range(0,r):
            if n[i]==n[l-1-i]:
                s+=1
        if s==r: return True
    else: return False
    
assert(palindrome(9009))  
assert(plusgros(2)==9009)
print(plusgros(3))
