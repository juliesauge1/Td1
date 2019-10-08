def lychrel(n):
    inv=''
    for i in range(50):
        inv=str(n)[::-1]
        n+=(int(inv))
        if palindrome(n):return False
        else:return True
	

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
    else:return False
    

def somme(n):
    s=0
    for i in range(n):
        if lychrel(i):
            s+=1
    return s


assert(lychrel(196))