def print_grid_2048(Gametab):   #prend le tableau de jeu et le convertis en grille a afficher
    val = []
    for i in range(len(Gametab)):
        val.append(Gametab[i])
        
    for i in range(len(Gametab)):
        if val[i] % 10 == val[i]:
            val[i] = ("  " + str(val[i]) + " ")
        elif val[i] % 100 == val[i]:
            val[i] = (" " + str(val[i]) + " ")
        elif val[i] % 1000 == val[i]:
            val[i] = (" " + str(val[i]) + "")
        else:
            val[i] = ("" + str(val[i]) + "")
    print("\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(val[0], val[1], val[2],val[3]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(val[4], val[5], val[6],val[7]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(val[8], val[9], val[10],val[11]))
    print("\t________|________|________|________\n\t        |        |        |\n\t  {}  |  {}  |  {}  |  {}  ".format(val[12], val[13], val[14],val[15]))
    print("\t        |        |        |\n")
    
Gametab=[]
def create_grid(Gametab):
    size = 4
    for i in range(size*size):
        Gametab.append(2000)
        
create_grid(Gametab)
print_grid_2048(Gametab)