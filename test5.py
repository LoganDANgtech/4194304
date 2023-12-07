l = [2, 0, 4, 4, 
     2, 0, 4, 4, 
     2, 0, 4, 4, 
     2, 0, 0, 0]

siez = 4

def get_coord(i, j):
    return i * siez + j

def gauche():
    row: int = 0
    while row < siez:
        col: int = 0
        while col < siez:
            value_col = l[get_coord(row, col)]
            search_index: int = col + 1

            while search_index < siez:
                value_search = l[get_coord(row, search_index)]
                if value_search == 0:
                    search_index += 1
                    continue

                if value_col != 0 and value_search != value_col:
                    col += 1
                    break

                l[get_coord(row, col)] += l[get_coord(row, search_index)]
                l[get_coord(row, search_index)] = 0

                if value_col == value_search:
                    col += 1

                break
            else:
                col += 1

        row += 1

gauche()

for i in range(4):
    for j in range(4):
        print(l[get_coord(i, j)], end = "" )
    print("")