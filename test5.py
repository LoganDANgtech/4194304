Gametab = [ 2, 0, 4, 4, 
            2, 0, 4, 4, 
            2, 0, 4, 4, 
            2, 0, 0, 0]

SIEZ = 4

def get1DCoord(i, j):
    return i * SIEZ + j
def getValue(Gametab : list[int], i : int, j : int) -> int:
    return Gametab[get1DCoord(i, j)]
def setValue(Gametab : list[int], i : int, j : int, value : int):
    Gametab[get1DCoord(i, j)] = value

def left():
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

def right():
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

def up():
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

def down():
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

left()

for i in range(4):
    for j in range(4):
        print(getValue(Gametab, i, j), end = "" )
    print("")