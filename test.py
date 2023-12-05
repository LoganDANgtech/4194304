import random
siez = 4
liste=[0,2,4,8]
l = [0,2,2,4,8,4,4,0,0,2,2,2,2,4,4,0]
# random.choice(liste) for _ in range(siez**2)
j=0
for i in range(siez):
    print(l[i*siez:siez*(i+1)])
print("\n")


def droite(j):
    while j < siez:
        i=siez-1
        while i !=0:
            if l[siez*j+i]==0 and l[siez*j+i-1]!=0:
                l[siez*j+i],l[siez*j+i-1]=l[siez*j+i-1],l[siez*j+i]
                if i<siez-1:
                    i += 1
            else:
                i-= 1
        for w in range(siez-2,-1,-1):
            if l[siez*j+w]==l[siez*j+w+1]:
                l[siez*j+w+1],l[siez*j+w]=2*l[siez*j+w],0
        i=siez-1
        while i !=0:
            if l[siez*j+i]==0 and l[siez*j+i-1]!=0:
                l[siez*j+i],l[siez*j+i-1]=l[siez*j+i-1],l[siez*j+i]
                if i<siez-1:
                    i += 1
            else:
                i-= 1
        j+=1
    return l


def gauche(j):
    while j < siez:
        i=0
        while i !=siez-1:
            if l[siez*j+i]==0 and l[siez*j+i+1]!=0:
                l[siez*j+i],l[siez*j+i+1]=l[siez*j+i+1],l[siez*j+i]
                if i>0:
                    i -= 1
            else:
                i+= 1
        for w in range(1,siez):
            if l[siez*j+w]==l[siez*j+w-1]:
                l[siez*j+w-1],l[siez*j+w]=2*l[siez*j+w],0
        i=0
        while i !=siez-1:
            if l[siez*j+i]==0 and l[siez*j+i+1]!=0:
                l[siez*j+i],l[siez*j+i+1]=l[siez*j+i+1],l[siez*j+i]
                if i>0:
                    i -= 1
            else:
                i+= 1
        j+=1
    return l


print(gauche(j))