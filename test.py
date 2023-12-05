import random
from math import *

liste=[0,2,4,8]
Gametab = [0,2,2,4,8,4,4,0,0,2,2,2,2,4,4,0]
siez = int(sqrt(len(Gametab)))
# random.choice(liste) for _ in range(siez**2)
r=0
c=0
for i in range(siez):
    print(Gametab[i*siez:siez*(i+1)])
print("\n")


def droite(r):
    while r < siez:
        c=siez-1
        while c !=0:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c-1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c-1]=Gametab[siez*r+c-1],Gametab[siez*r+c]
                if c<siez-1:
                    c += 1
            else:
                c-= 1
        for i in range(siez-2,-1,-1):
            if Gametab[siez*r+i]==Gametab[siez*r+i+1]:
                Gametab[siez*r+i+1],Gametab[siez*r+i]=2*Gametab[siez*r+i],0
        c=siez-1
        while c !=0:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c-1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c-1]=Gametab[siez*r+c-1],Gametab[siez*r+c]
                if c<siez-1:
                    c += 1
            else:
                c-= 1
        r+=1
    return Gametab


def gauche(r):
    while r < siez:
        c=0
        while c !=siez-1:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c+1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c+1]=Gametab[siez*r+c+1],Gametab[siez*r+c]
                if c>0:
                    c -= 1
            else:
                c+= 1
        for i in range(1,siez):
            if Gametab[siez*r+i]==Gametab[siez*r+i-1]:
                Gametab[siez*r+i-1], Gametab[siez*r+i] = 2*Gametab[siez*r+i], 0
        c=0
        while c !=siez-1:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c+1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c+1]=Gametab[siez*r+c+1],Gametab[siez*r+c]
                if c>0:
                    c -= 1
            else:
                c+= 1
        r+=1
    return Gametab


def haut(c):
    while c < siez:
        r=0
        while r !=siez-1:
            if Gametab[siez*c+r]==0 and Gametab[siez*(c+1)+r]!=0:
                Gametab[siez*c+r],Gametab[siez*(c+1)+r]=Gametab[siez*(c+1)+r],Gametab[siez*c+r]
                if r>0:
                    r -= 1
            else:
                r+= 1
        for i in range(1,siez):
            if Gametab[siez*c+i]==Gametab[siez*c+i-1]:
                Gametab[siez*c+i-1], Gametab[siez*c+i] = 2*Gametab[siez*c+i], 0
        r=0
        while r !=siez-1:
            if Gametab[siez*c+r]==0 and Gametab[siez*(c+1)+r]!=0:
                Gametab[siez*c+r],Gametab[siez*(c+1)+r]=Gametab[siez*(c+1)+r],Gametab[siez*c+r]
                if r>0:
                    r -= 1
            else:
                r+= 1
        c+=1
    for i in range(siez):
        print(Gametab[i*siez:siez*(i+1)])


print(haut(r))