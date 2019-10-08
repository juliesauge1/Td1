def exo1(n):
    s=0
    for i in range (n) :
        if i%5==0 or i%3==0:
            s+=i
    return s 



assert exo1(10)==23
print(exo1(1000))
