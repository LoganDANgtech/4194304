import random
siez = 16
liste=[0,2,4,8]
l = [random.choice(liste) for _ in range(siez**2)]
leng=len(l)//siez
i=leng-1
j=0
print(l)
while j < leng:
    i=leng-1
    while i !=0:
        if l[leng*j+i]==0 and l[leng*j+i-1]!=0:
            l[leng*j+i],l[leng*j+i-1]=l[leng*j+i-1],l[leng*j+i]
            if i<siez-1:
                i += 1
        else:
            i-= 1
    for w in range(leng-2,-1,-1):
        if l[leng*j+w]==l[leng*j+w+1]:
            l[leng*j+w+1],l[leng*j+w]=2*l[leng*j+w],0
    i=leng-1
    while i !=0:
        if l[leng*j+i]==0 and l[leng*j+i-1]!=0:
            l[leng*j+i],l[leng*j+i-1]=l[leng*j+i-1],l[leng*j+i]
            if i<siez-1:
                i += 1
        else:
            i-= 1
    j+=1
print(l)
















# from time import *
# siez = 1024
# l = [4 for _ in range(siez*siez)]
# leng=len(l)
# chrono = time()
# for j in range(siez):
#     while 0 in l:
#         l.pop(l.index(0))
#     for i in range(len(l)-2,-1,-1):
#         if l[i]==l[i+1]:
#             l[i+1],l[i]=2*l[i],0
#     while 0 in l:
#         l.pop(l.index(0))
#     while leng!=len(l):
#         l.insert(0,0)
# print(time()-chrono,l)