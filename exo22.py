def score(nom):
    s=0
    for i in nom:
        s+=ord(i)-64
    return s

def exo22(doc):
    s=0
    total=0
    fichier=open('p022_names.txt')
    noms=list(eval(fichier.read()))
    fichier.close()
    noms.sort()
    for i in range(0,len(noms)):
        s=(score(noms[i])*(i+1))
        total+=s    
    return total
    
print(exo22('p022_name'))    
        
        
        
        
        



