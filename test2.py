from random import randint
import keyboard

def print_grid_2048():   #prend le tableau de jeu et le convertis en grille a afficher
    printtab = []
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
    print("\t        |        |        |\n")
    
def Loose():
    print("tié mové")
    print(print_grid_2048)
    return
    


def left():
    for i in range(size):
        for j in range(size):
            val = Gametab[(i*size) + j]
            if not(val == "0"):
                pos_to_verif = j - 1
                while Gametab[(i*size) + pos_to_verif] == "0":
                    pos_to_verif = pos_to_verif - 1
                    
                if not(Gametab[(i*size) + pos_to_verif] == "0"):
                    num_here : bool = True
                elif pos_to_verif == 0:
                    num_here : bool = False
                    
                if num_here:
                    
                    if Gametab[(i*size) + pos_to_verif] == val:
                        Gametab[(i*size) + pos_to_verif] = str(int(val*2))
                        Gametab[(i*size) + j] = "0"
                    else:
                        Gametab[(i*size) + pos_to_verif + 1] == str(val)
                        Gametab[(i*size) + j] = "0"
                        
                else:
                    Gametab[(i*size) + pos_to_verif] = val
                    Gametab[(i*size) + j] = "0"   
                
                        
                        

def right():
    siez = 4
    leng=len(Gametab)//siez
    i=leng-1
    j=0
    while j < leng:
        i=leng-1
        while i !=0:
            if Gametab[leng*j+i]==0 and Gametab[leng*j+i-1]!=0:
                Gametab[leng*j+i],Gametab[leng*j+i-1]=Gametab[leng*j+i-1],Gametab[leng*j+i]
                if i<siez-1:
                    i += 1
            else:
                i-= 1
        for w in range(leng-2,-1,-1):
            if Gametab[leng*j+w]==Gametab[leng*j+w+1]:
                Gametab[leng*j+w+1],Gametab[leng*j+w]=2*Gametab[leng*j+w],0
        i=leng-1
        while i !=0:
            if Gametab[leng*j+i]==0 and Gametab[leng*j+i-1]!=0:
                Gametab[leng*j+i],Gametab[leng*j+i-1]=Gametab[leng*j+i-1],Gametab[leng*j+i]
                if i<siez-1:
                    i += 1
            else:
                i-= 1
        j+=1

def up():
    pass
def down():
    pass

def chck_pos_libre(pos_libre):
    pos_libre.clear()
    for i in range(len(Gametab)-1):
        if Gametab[i] == 0:
            pos_libre.append(i)
    if pos_libre == []:
        return False
    else:
        return True
    
def addnumber(pos_libre):
    print(pos_libre)
    pos = pos_libre[ randint(0,len(pos_libre) - 1) ]
    
    _2or4 = randint(1,10)
    print(pos)
    if _2or4 == 1:
        Gametab[pos] = 4
    else:
        Gametab[pos] = 2
    
def create_grid(size):
    for i in range(size*size):
        Gametab.append(0)

def turn(Game):
    pos_libre = []
    if not(chck_pos_libre(pos_libre)):
        Game = Loose()
    addnumber(pos_libre)
    print_grid_2048()

size = 4
Gametab=[]
create_grid(size)
Game = True
while Game == True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q' :    #gauche
        left()
        turn(Game)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'd' :    #droite
        right()
        turn(Game)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'z' :    #haut
        up()
        turn(Game)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :    #bas
        down()
        turn(Game)