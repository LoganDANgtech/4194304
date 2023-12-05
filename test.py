from random import randint
import keyboard
import os
from time import *
from _2048txt import print2048
SIEZ: int = 15

# 57 \n /// sqrt = 9*\n /// 1*\n oblg /// 1 lignes == 3 * \n

def print_grid_2048(Gametab : list[int]):
    os.system("cls")
    printtab : list = []
    for i in range(len(Gametab)):
        if Gametab[i] == 0:            
            printtab.append("     ")
        else:
            printtab.append(Gametab[i])
            
    for i in range(len(Gametab)):
        if printtab[i] == "     ":
            pass
        elif int(printtab[i]) % 10 == int(printtab[i]):
            printtab[i] = ("  " + str(printtab[i]) + "  ")
        elif int(printtab[i]) % 100 == int(printtab[i]):
            printtab[i] = (" " + str(printtab[i]) + "  ")
        elif int(printtab[i]) % 1000 == int(printtab[i]):
            printtab[i] = (" " + str(printtab[i]) + " ")
        elif int(printtab[i]) % 10000 == int(printtab[i]):
            printtab[i] = (" " + str(printtab[i]) + "")
        else:
            printtab[i] = ("" + str(printtab[i]) + "")

    if SIEZ < 16:
        print2048()

    opretation_n = (45+(9*(SIEZ>=16))-(SIEZ*3))//2
    opretation_t = (260-(SIEZ*10))//2
    

    print("\n"*opretation_n)
    for j in range(SIEZ-1):
        print(" "*(opretation_t),end="")
        for _ in range (SIEZ-1):
            print("         |" , end = "")

        print("\n"+" "*(opretation_t),end="")
        for i in range (SIEZ - 1):
            print("  {}  |".format(printtab[get1DCoord(j,i)]), end = "")
        print("  {}  ".format(printtab[get1DCoord(j,SIEZ-1)]))

        print(" "*(opretation_t),end="")
        for _ in range (SIEZ - 1):
            print("_________|" , end = "")
        print("__________")

    print(" "*(opretation_t),end="")
    for _ in range (SIEZ-1):
        print("         |" , end = "")
        
    print("\n"+" "*(opretation_t),end="")
    for i in range (SIEZ - 1):
        print("  {}  |".format(printtab[get1DCoord(SIEZ-1,i)]), end = "")
    print("  {}  ".format(printtab[get1DCoord(SIEZ-1,SIEZ-1)]))

    print(" "*(opretation_t),end="")
    for _ in range (SIEZ-1):
        print("         |" , end = "")

    print()

def left(Gametab : list[int]) -> int:
    c : int = 0         #column
    r : int = 0         #row
    nb_modif : int = 0

    while r < SIEZ:
        c=0
        while c !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c+1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c+1))
                setValue(Gametab, r, c+1, 0)
                nb_modif += 1
                if c>0:
                    c -= 1
            else:
                c+= 1
        for i in range(1,SIEZ):
            if getValue(Gametab, r, i)==getValue(Gametab, r, i-1):
                setValue(Gametab, r, i-1, 2*getValue(Gametab, r, i))
                setValue(Gametab, r, i, 0)
                nb_modif += 1
        c=0
        while c !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c+1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c+1))
                setValue(Gametab, r, c+1, 0)
                nb_modif += 1
                if c>0:
                    c -= 1
            else:
                c+= 1
        r+=1
    return nb_modif 

def right(Gametab : list[int]) -> int:
    c : int =SIEZ-1    #column
    r : int =0         #row
    nb_modif : int = 0

    while r < SIEZ:
        c=SIEZ-1
        while c !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c-1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c-1))
                setValue(Gametab, r, c-1, 0)
                nb_modif += 1
                if c<SIEZ-1:
                    c += 1
            else:
                c-= 1
        for i in range(SIEZ-2,-1,-1):
            if getValue(Gametab, r, i)==getValue(Gametab, r, i+1):
                setValue(Gametab, r, i+1, 2*getValue(Gametab, r, i))
                setValue(Gametab, r, i, 0)
                nb_modif += 1
        c=SIEZ-1
        while c !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c-1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c-1))
                setValue(Gametab, r, c-1, 0)
                nb_modif += 1
                if c<SIEZ-1:
                    c += 1
            else:
                c-= 1
        r+=1

    return nb_modif

def up(Gametab : list[int]) -> int:
    c : int = 0
    r : int = 0
    nb_modif = 0
    while c < SIEZ:
        r=0
        while r !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r+1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r+1, c))
                setValue(Gametab, r+1, c, 0)
                nb_modif += 1
                if r>0:
                    r -= 1
            else:
                r+= 1
        for i in range(1,SIEZ):
            if getValue(Gametab, i, c)==getValue(Gametab, i-1, c):
                setValue(Gametab, i-1, c, 2*getValue(Gametab, i, c))
                setValue(Gametab, i, c, 0)
                nb_modif += 1
        r=0
        while r !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r+1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r+1, c))
                setValue(Gametab, r+1, c, 0)
                nb_modif += 1
                if r>0:
                    r -= 1
            else:
                r+= 1
        c+=1
    return nb_modif

def down(Gametab : list[int]) -> int:
    c : int = 0
    r : int = SIEZ-1
    nb_modif = 0
    while c < SIEZ:
        r=SIEZ-1
        while r !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r-1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r-1, c))
                setValue(Gametab, r-1, c, 0)
                nb_modif += 1
                if r<SIEZ-1:
                    r += 1
            else:
                r-= 1
        for i in range(SIEZ-2,-1,-1):
            if getValue(Gametab, i, c)==getValue(Gametab, i+1, c):
                setValue(Gametab, i+1, c, 2*getValue(Gametab, i, c))
                setValue(Gametab, i, c, 0)
                nb_modif += 1
        r=SIEZ-1
        while r !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r-1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r-1, c))
                setValue(Gametab, r-1, c, 0)
                nb_modif += 1
                if r<SIEZ-1:
                    r += 1
            else:
                r-= 1
        c+=1
    return nb_modif

def chck_pos_libre(pos_libre : list, Gametab : list[int]) -> bool:
    pos_libre.clear()
    for i in range(len(Gametab)):
        if Gametab[i] == 0:
            pos_libre.append(i)
    
    return len(pos_libre) > 0
    
def addnumber(pos_libre : list, Gametab : list[int]) -> list:
    pos = pos_libre[ randint(0,len(pos_libre) - 1) ]
    _2or4 = randint(1,10)

    if _2or4 == 1:
        Gametab[pos] = 4
    else:
        Gametab[pos] = 2


def get1DCoord(i : int, j : int) -> int:
    return i * SIEZ + j
def getValue(Gametab : list[int], i : int, j : int) -> int:
    return Gametab[get1DCoord(i, j)]
def setValue(Gametab : list[int], i : int, j : int, value : int):
    Gametab[get1DCoord(i, j)] = value


def create_grid(Gametab : list[int]) -> list:
    for _ in range(SIEZ**2):
        Gametab.append(0)

def turn(nb_modif : int , Gametab : list[int]) -> bool:
    pos_libre = []
    if not(chck_pos_libre(pos_libre , Gametab)) and nb_modif == 0:
        return False
    if nb_modif > 0:
        addnumber(pos_libre, Gametab)
    print_grid_2048(Gametab)
    
    return True

def __main__():
    Gametab = []
    nb_modif = 1
    create_grid(Gametab)
    turn(nb_modif, Gametab)
    Game = True
    while Game == True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'q' or event.name == 'Q') :    #gauche
            chrono = time()
            nb_modif = left(Gametab)
            Game = turn(nb_modif, Gametab)
            # print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'd' or event.name == 'D') :    #droite
            chrono = time()
            nb_modif = right(Gametab)
            Game = turn(nb_modif, Gametab)
            # print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'z' or event.name == 'Z') :    #haut
            chrono = time()
            nb_modif =  up(Gametab)
            Game = turn(nb_modif, Gametab)
            # print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 's' or event.name == 'S' or event.name == 'space') :    #bas
            chrono = time()
            nb_modif = down(Gametab)
            Game = turn(nb_modif, Gametab)
            # print(time() - chrono)
        
    print("tiémové")

__main__()