SIEZ: int = 4

def get1DCoord(i : int, j : int) -> int:
    return i * SIEZ + j
def getValue(Gametab : list[int], i : int, j : int) -> int:
    return Gametab[get1DCoord(i, j)]
def setValue(Gametab : list[int], i : int, j : int, value : int):
    Gametab[get1DCoord(i, j)] = value

SIEZ = 4

def get1DCoord(i, j):
    return i * SIEZ + j
def getValue(Gametab : list[int], i : int, j : int) -> int:
    return Gametab[get1DCoord(i, j)]
def setValue(Gametab : list[int], i : int, j : int, value : int):
    Gametab[get1DCoord(i, j)] = value

def left(Gametab):
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
    return Gametab

def right(Gametab):
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
    return Gametab

def up(Gametab):
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
    return Gametab

def down(Gametab):
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
    return Gametab

tests : dict[list[list[int],list[int]]] = {        #1: nom de la situation, 2: situation , 3: solution attendue
    "fusion simple(haut)":
    [[
        2,0,0,0,
        2,0,0,0,
        0,0,0,0,
        0,0,0,0
    ],[
        4,0,0,0,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ]]
    ,"non fusion(gauche)":
    [[
        4,2,0,0,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ],[
        4,2,0,0,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ]]
    ,"non fusion éloignée(droite)":
    [[
        0,2,0,4,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ],[
        0,0,2,4,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ]]
    ,"fusion éloignée(bas)":
    [[
        2,0,0,0,
        0,0,0,0,
        0,0,0,0,
        2,0,0,0
    ],
     [
        0,0,0,0,
        0,0,0,0,
        0,0,0,0,
        4,0,0,0
    ]]
    ,"double fusion(haut)":
    [[
        0,0,0,2,
        0,0,0,2,
        0,0,0,2,
        0,0,0,2
    ],[
        0,0,0,4,
        0,0,0,4,
        0,0,0,0,
        0,0,0,0
    ]]
    ,"decalage vers le bas(bas)":
    [[
        0,0,0,2,
        0,0,0,4,
        0,0,0,2,
        0,0,0,0
    ],[
        0,0,0,0,
        0,0,0,2,
        0,0,0,4,
        0,0,0,2
    ]]
    ,"décalage vers la gauche et fusion(gauche)":
    [[
        0,0,0,0,
        0,0,0,0,
        0,0,0,0,
        0,4,2,2
    ],[
        0,0,0,0,
        0,0,0,0,
        0,0,0,0,
        4,4,0,0
    ]]
    }

def test(dico_test: dict):
    relateTo: list = ["fusion simple(haut)","non fusion(gauche)","non fusion éloignée(droite)","fusion éloignée(bas)","double fusion(haut)","decalage vers le bas(bas)","décalage vers la gauche et fusion(gauche)"]
    User: str = input("Que voulez vous faire ? fusion simple(haut), non fusion(gauche), non fusion éloignée(droite), fusion éloignée(bas), double fusion(haut), decalage vers le bas(bas), décalage vers la gauche et fusion(gauche)")
    while User not in "1234567":
        User: str = input("Que voulez vous faire ? fusion simple(haut), non fusion(gauche), non fusion éloignée(droite), fusion éloignée(bas), double fusion(haut), decalage vers le bas(bas), décalage vers la gauche et fusion(gauche)")
    if User == "1":
        Result: list = up(dico_test[relateTo[int(User)-1 ]][0])
    elif User == "2":
        Result: list = left(dico_test[relateTo[int(User)-1]][0])
    elif User == "3":
        Result: list = right(dico_test[relateTo[int(User)-1]][0])
    elif User == "4":
        Result: list = down(dico_test[relateTo[int(User)-1]][0])
    elif User == "5":
        Result: list = up(dico_test[relateTo[int(User)-1]][0])
    elif User == "6":
        Result: list = down(dico_test[relateTo[int(User)-1]][0])
    elif User == "7":
        Result: list = left(dico_test[relateTo[int(User)-1]][0])
    return Result==dico_test[relateTo[int(User)-1]][1]

print(test(tests))