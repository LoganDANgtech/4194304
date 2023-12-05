from time import *
siez = 1024
l = [4 for _ in range(siez*siez)]
leng=len(l)
chrono = time()
for j in range(siez):
    while 0 in l:
        l.pop(l.index(0))
    for i in range(len(l)-2,-1,-1):
        if l[i]==l[i+1]:
            l[i+1],l[i]=2*l[i],0
    while 0 in l:
        l.pop(l.index(0))
    while leng!=len(l):
        l.insert(0,0)
print(time()-chrono,l)