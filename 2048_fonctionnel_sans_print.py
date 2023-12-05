from random import randint
import keyboard
SIEZ: int = 4

def print_grid_2048(Gametab : list[int]):
    for i in range(SIEZ):
        print(Gametab[i*SIEZ:SIEZ*(i+1)])
    print("")
    print("")
    print("")

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
                if c>0:
                    c -= 1
            else:
                c+= 1
        for i in range(1,SIEZ):
            if getValue(Gametab, r, i)==getValue(Gametab, r, i-1):
                setValue(Gametab, r, i-1, 2*getValue(Gametab, r, i))
                setValue(Gametab, r, i, 0)
        c=0
        while c !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c+1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c+1))
                setValue(Gametab, r, c+1, 0)
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
                if c<SIEZ-1:
                    c += 1
            else:
                c-= 1
        for i in range(SIEZ-2,-1,-1):
            if getValue(Gametab, r, i)==getValue(Gametab, r, i+1):
                setValue(Gametab, r, i+1, 2*getValue(Gametab, r, i))
                setValue(Gametab, r, i, 0)
        c=SIEZ-1
        while c !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r, c-1)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r, c-1))
                setValue(Gametab, r, c-1, 0)
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
                if r>0:
                    r -= 1
            else:
                r+= 1
        for i in range(1,SIEZ):
            if getValue(Gametab, i, c)==getValue(Gametab, i-1, c):
                setValue(Gametab, i-1, c, 2*getValue(Gametab, i, c))
                setValue(Gametab, i, c, 0)
        r=0
        while r !=SIEZ-1:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r+1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r+1, c))
                setValue(Gametab, r+1, c, 0)
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
                if r<SIEZ-1:
                    r += 1
            else:
                r-= 1
        for i in range(SIEZ-2,-1,-1):
            if getValue(Gametab, i, c)==getValue(Gametab, i+1, c):
                setValue(Gametab, i+1, c, 2*getValue(Gametab, i, c))
                setValue(Gametab, i, c, 0)
        r=SIEZ-1
        while r !=0:
            if getValue(Gametab, r, c)==0 and getValue(Gametab, r-1, c)!=0:
                setValue(Gametab, r, c, getValue(Gametab, r-1, c))
                setValue(Gametab, r-1, c, 0)
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
    addnumber(pos_libre, Gametab)
    print_grid_2048(Gametab)
    
    return True

def __main__():
    Gametab = []
    create_grid(Gametab)
    Game = True
    while Game == True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'q' or event.name == 'Q') :    #gauche
            nb_modif = left(Gametab)
            Game = turn(nb_modif, Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'd' or event.name == 'D') :    #droite
            nb_modif = right(Gametab)
            Game = turn(nb_modif, Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 'z' or event.name == 'Z') :    #haut
            nb_modif =  up(Gametab)
            Game = turn(nb_modif, Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and (event.name == 's' or event.name == 'S') :    #bas
            nb_modif = down(Gametab)
            Game = turn(nb_modif, Gametab)
        
    print("tiémové")

__main__()