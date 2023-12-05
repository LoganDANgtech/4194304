from random import randint
import keyboard

SIZE: int = 4

def print_grid_2048(Gametab : list):   #prend le tableau de jeu et le convertis en grille a afficher
    printtab : list = []
    for i in range(len(Gametab)):
        if Gametab[i] == 0:            
            printtab.append("    ")
        else:
            printtab.append(Gametab[i])
            
    for i in range(len(Gametab)):
        if printtab[i] == "    ":
            pass
        elif int(printtab[i]) % 10 == int(printtab[i]):
            printtab[i] = ("  " + str(printtab[i]) + " ")
        elif int(printtab[i]) % 100 == int(printtab[i]):
            printtab[i] = (" " + str(printtab[i]) + " ")
        elif int(printtab[i]) % 1000 == int(printtab[i]):
            printtab[i] = (" " + str(printtab[i]) + "")
        else:
            printtab[i] = ("" + str(printtab[i]) + "")
    print("\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(printtab[0], printtab[1], printtab[2],printtab[3]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(printtab[4], printtab[5], printtab[6],printtab[7]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(printtab[8], printtab[9], printtab[10],printtab[11]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(printtab[12], printtab[13], printtab[14],printtab[15]))
    print("\t        |        |        |\n\n\n")

def left(siez : int , Gametab) -> int:
    c : int = 0         #column
    r : int = 0         #row
    nb_modif : int = 0
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
                Gametab[siez*r+i-1],Gametab[siez*r+i]=2*Gametab[siez*r+i],0
        c=0
        while c !=siez-1:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c+1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c+1]=Gametab[siez*r+c+1],Gametab[siez*r+c]
                if c>0:
                    c -= 1
            else:
                c+= 1
        r+=1
    return nb_modif 
                
                        
                        
def get1DCoord(i, j):
    return i * SIZE + j

def getValue(Gametab, i, j):
    return Gametab(get1DCoord(i, j))

def setValue(Gametab, i, j, value):
    Gametab(get1DCoord(i, j)) = value


def right(siez : int , Gametab) -> int:
    c : int =siez-1    #column
    r : int =0         #row
    nb_modif : int = 0
    while r < siez:
        c=siez-1
        while c !=0:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c-1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c-1]=Gametab[siez*r+c-1],Gametab[siez*r+c]
                nb_modif += 1
                if c<siez-1:
                    c += 1
            else:
                c-= 1
        for i in range(siez-2,-1,-1):
            if Gametab[siez*r+i]==Gametab[siez*r+i+1]:
                Gametab[siez*r+i+1],Gametab[siez*r+i]=2*Gametab[siez*r+i],0
                nb_modif += 1
        c=siez-1
        while c !=0:
            if Gametab[siez*r+c]==0 and Gametab[siez*r+c-1]!=0:
                Gametab[siez*r+c],Gametab[siez*r+c-1]=Gametab[siez*r+c-1],Gametab[siez*r+c]
                nb_modif += 1
                if c<siez-1:
                    c += 1
            else:
                c-= 1
        r+=1
    return nb_modif

def up(siez : int , Gametab) -> int:
    nb_modif = 0
    return nb_modif
def down(siez : int , Gametab) -> int:
    nb_modif = 0
    return nb_modif

def chck_pos_libre(pos_libre : list , Gametab) -> bool:
    pos_libre.clear()
    for i in range(len(Gametab)):
        if Gametab[i] == 0:
            pos_libre.append(i)
    
    return len(pos_libre) > 0
    
def addnumber(pos_libre : list , Gametab) -> list:
    pos = pos_libre[ randint(0,len(pos_libre) - 1) ]
    _2or4 = randint(1,10)

    if _2or4 == 1:
        Gametab[pos] = 4
    else:
        Gametab[pos] = 2

    return Gametab
    
def create_grid(siez : int , Gametab : list) -> list:
    for i in range(siez*siez):
        Gametab.append(0)
    return Gametab

def turn(nb_modif : int , Gametab : list) -> bool:
    pos_libre = []
    if not(chck_pos_libre(pos_libre , Gametab : list)) and nb_modif == 0:
        return False
    addnumber(pos_libre)
    print_grid_2048()
    return True

def __main__():
    siez = 4
    Gametab=[]
    create_grid(siez , Gametab)
    Game = True
    while Game == True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'q' :    #gauche
            nb_modif = left(siez , Gametab)
            Game = turn(nb_modif , Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and event.name == 'd' :    #droite
            nb_modif = right(siez , Gametab)
            Game = turn(nb_modif , Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and event.name == 'z' :    #haut
            nb_modif =  up(siez , Gametab)
            Game = turn(nb_modif , Gametab)
            
        if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :    #bas
            nb_modif = down(siez , Gametab)
            Game = turn(nb_modif , Gametab)
        
    print("tiémové")

__main__()