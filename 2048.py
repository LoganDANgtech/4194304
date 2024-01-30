from random import random , randint
import keyboard
import os
from time import *
from _2048txt import print2048
SIEZ: int = 4

def print_grid_2048(Gametab : list[int]):
    os.system("cls")
    printtab : list = []
    for i in range(len(Gametab)):
        if Gametab[i] == 0:            
            printtab.append("         ")
        else:
            printtab.append(Gametab[i])
            
    for i in range(len(Gametab)):
        code_couleur : str = ""
        if printtab[i] == "         ": 
            pass
        elif int(printtab[i]) % 10 == int(printtab[i]):
            if int(printtab[i]) <= 2:
                code_couleur = "\x1b[48;2;238;228;218m    "
            elif int(printtab[i]) <= 4:
                code_couleur = "\x1b[48;2;238;225;201m    "
            elif int(printtab[i]) <= 8:
                code_couleur = "\x1b[48;2;243;178;122m    "
            printtab[i] = (code_couleur + str(printtab[i]) +"    \x1b[49m")
        elif int(printtab[i]) % 100 == int(printtab[i]):
            if int(printtab[i]) <= 16:
                code_couleur = "\x1b[48;2;246;150;100m    "
            elif int(printtab[i]) <= 32:
                code_couleur = "\x1b[48;2;247;126;95m    "
            elif int(printtab[i]) <= 64:
                code_couleur = "\x1b[48;2;247;95;59m    "
            printtab[i] = (code_couleur + str(printtab[i]) + "   \x1b[49m")
        elif int(printtab[i]) % 1000 == int(printtab[i]):
            if int(printtab[i]) <= 128:
                code_couleur = "\x1b[48;2;237;208;115m   "
            elif int(printtab[i]) <= 256:
                code_couleur = "\x1b[48;2;237;204;98m   "
            elif int(printtab[i]) <= 512:
                code_couleur = "\x1b[48;2;237;201;80m   "
            printtab[i] = (code_couleur + str(printtab[i])+"   \x1b[49m")
        elif int(printtab[i]) % 10000 == int(printtab[i]):
            if int(printtab[i]) <= 1024:
                code_couleur = "\x1b[48;2;237;197;63m   "
            elif int(printtab[i]) <= 2048:
                code_couleur = "\x1b[48;2;237;194;46m   "
            elif int(printtab[i]) >= 2045:
                code_couleur = "\x1b[48;2;60;58;51m   "
            printtab[i] = (code_couleur + str(printtab[i])+"  \x1b[49m")
        else:
            code_couleur = "\x1b[48;2;60;58;51m  "
            printtab[i] = (code_couleur + str(printtab[i])+"  \x1b[49m")

    if SIEZ < 16:
        print2048()
    characterrandom = ["♥","¸","?","✂","♛"]
    characterchosen = characterrandom[randint(0,len(characterrandom)-1)]
    opretation_n = (45+(9*(SIEZ>=16))-(SIEZ*3))//2-1
    opretation_t = (260-(SIEZ*10))//2
    if opretation_n>0:
        print("\n"*(opretation_n))
    print(" "*(opretation_t)+ characterchosen + "_________",end="")
    for _ in range (SIEZ-1):
        print("__________" , end = "")
    print(characterchosen +" "*(opretation_t))
    for j in range(SIEZ):
        print(" "*(opretation_t),end="")
        for _ in range (SIEZ):
            print("|         " , end = "")
        print("|\n"+" "*(opretation_t),end="")
        for i in range (SIEZ - 1):
            print("|{}".format(printtab[get1DCoord(j,i)]), end = "")
        print("|{}|".format(printtab[get1DCoord(j,SIEZ-1)]))

        print(" "*(opretation_t),end="")
        for _ in range (SIEZ - 1):
            print("|_________" , end = "")
        print("|_________|")
        
    print("\n"*(opretation_n))

def left(Gametab : list[int]):
    r: int = 0
    nb_modif: int = 0
    while r < SIEZ:
        c: int = 0
        while c < SIEZ:
            value_col: int = getValue(Gametab, r, c)
            search_index: int = c + 1

            while search_index < SIEZ:
                value_search: int = getValue(Gametab, r, search_index)
                if value_search == 0:
                    search_index += 1
                    continue

                if value_col != 0 and value_search != value_col:
                    c += 1
                    break

                setValue(Gametab, r, c, getValue(Gametab, r, c) + getValue(Gametab, r, search_index))
                setValue(Gametab, r, search_index, 0)
                nb_modif += 1

                if value_col == value_search:
                    c += 1

                break
            else:
                c += 1

        r += 1
    return nb_modif

def right(Gametab : list[int]):
    r: int = 0
    nb_modif: int = 0
    while r < SIEZ:
        c: int = SIEZ - 1
        while c > -1 :
            value_col: int = getValue(Gametab, r, c)
            search_index: int = c - 1

            while search_index > -1 :
                value_search: int = getValue(Gametab, r, search_index)
                if value_search == 0:
                    search_index -= 1
                    continue

                if value_col != 0 and value_search != value_col:
                    c -= 1
                    break

                setValue(Gametab, r, c, getValue(Gametab, r, c) + getValue(Gametab, r, search_index))
                setValue(Gametab, r, search_index, 0)
                nb_modif += 1

                if value_col == value_search:
                    c -= 1

                break
            else:
                c -= 1

        r += 1
    return nb_modif

def up(Gametab : list[int]):
    c: int = 0
    nb_modif: int = 0
    while c < SIEZ:
        r: int = 0
        while r < SIEZ:
            value_col: int = getValue(Gametab, r, c)
            search_index: int = r + 1

            while search_index < SIEZ:
                value_search: int = getValue(Gametab, search_index, c)
                if value_search == 0:
                    search_index += 1
                    continue

                if value_col != 0 and value_search != value_col:
                    r += 1
                    break

                setValue(Gametab, r, c, getValue(Gametab, r, c) + getValue(Gametab, search_index, c))
                setValue(Gametab, search_index, c, 0)
                nb_modif += 1

                if value_col == value_search:
                    r += 1

                break
            else:
                r += 1

        c += 1
    return nb_modif

def down(Gametab : list[int]):
    c: int = 0
    nb_modif: int = 0
    while c < SIEZ:
        r: int = SIEZ - 1
        while r > -1:
            value_col: int = getValue(Gametab, r, c)
            search_index: int = r - 1

            while search_index > -1:
                value_search: int = getValue(Gametab, search_index, c)
                if value_search == 0:
                    search_index -= 1
                    continue

                if value_col != 0 and value_search != value_col:
                    r -= 1
                    break

                setValue(Gametab, r, c, getValue(Gametab, r, c) + getValue(Gametab, search_index, c))
                setValue(Gametab, search_index, c, 0)
                nb_modif += 1

                if value_col == value_search:
                    r -= 1

                break
            else:
                r -= 1

        c += 1
    return nb_modif

def chck_pos_libre(pos_libre : list, Gametab : list[int]) -> bool:
    pos_libre.clear()
    for i in range(len(Gametab)):
        if Gametab[i] == 0:
            pos_libre.append(i)
    
    return len(pos_libre) > 0
    
def addnumber(pos_libre : list, Gametab : list[int]) -> list:
    pos = pos_libre[ randint(0,len(pos_libre) - 1) ]
    
    luk = 0.1  #chance for a four to appear (in percent) 
    _2or4 = random()

    if _2or4 <= luk :
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
    if not(chck_pos_libre(pos_libre , Gametab)) and left(Gametab)==right(Gametab)==up(Gametab)==down(Gametab)==0:
        return False
    if nb_modif > 0:
        if len(pos_libre)==SIEZ**2:
            addnumber(pos_libre, Gametab)
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
            print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'd' or event.name == 'D') :    #droite
            chrono = time()
            nb_modif = right(Gametab)
            Game = turn(nb_modif, Gametab)
            print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'z' or event.name == 'Z') :    #haut
            chrono = time()
            nb_modif =  up(Gametab)
            Game = turn(nb_modif, Gametab)
            print(time() - chrono)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 's' or event.name == 'S' or event.name == 'space') :    #bas
            chrono = time()
            nb_modif = down(Gametab)
            Game = turn(nb_modif, Gametab)
            print(time() - chrono)

    print("tiémové")

__main__()