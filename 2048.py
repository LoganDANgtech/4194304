from random import randint
import keyboard

def print_grid_2048(Gametab):   #prend le tableau de jeu et le convertis en grille a afficher
    printtab = []
    for i in range(len(Gametab)):
        if Gametab[i] == "0":            
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



def left():
    for i in range(size):
        for j in range(size):
            val = Gametab[(i*size) + j]
            if j == 0:
                pass
            elif val == "0":
                pass
            elif not(val == "0"):
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
    pass
def up():
    pass
def down():
    pass



def addnumber(size):
    
    _2or4 = randint(1,10)
    pos = randint(0,(size*size)-1)
    while not(Gametab[pos] == "0"):
        pos = randint(0,(size*size)-1)
    
    if _2or4 == 1:
        Gametab[pos] = 4
    else:
        Gametab[pos] = 2
    

def create_grid(size):
    for i in range(size*size):
        Gametab.append("0")



size = 4
Gametab=[]
create_grid(size)

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q' :    #gauche
        left()
        addnumber(size)
        print_grid_2048(Gametab)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'd' :    #droite
        right()
        addnumber(size)
        print_grid_2048(Gametab)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'z' :    #haut
        up()
        addnumber(size)
        print_grid_2048(Gametab)
        
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :    #bas
        down()
        addnumber(size)
        print_grid_2048(Gametab)