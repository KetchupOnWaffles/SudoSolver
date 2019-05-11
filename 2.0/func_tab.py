#these functions in order, create the lists all, line, column and sq lists
from show import showff
def tout(f):
    tout = list()
    for i in f:
        l = i.strip()
        tout.extend(l)
    for i in tout:
        if i == " ":
            tout.remove(" ")
    for i in tout:
        if i != "V":
            tout[tout.index(i)] = int(i)
    return tout



#checks all cells if empty, see all possibilities, if only one, replace in all lists, this function is recursive so it can use new information for elimination
def liste_vides(all, line, column, sq):
    count = 0
    colnum = 0
    vi = list()
    for i in all:
        if i == "V":
            possible = [1,2,3,4,5,6,7,8,9]
            for j in line[int(count/9)]:
                for k in possible:
                    if j == k:
                        possible.remove(k)
            for j in column[colnum]:
                for k in possible:
                    if j == k:
                        possible.remove(k)
            if count in [0,1,2,9,10,11,18,19,20]:
                sqnum = 0
            elif count in [3,4,5,12,13,14,21,22,23]:
                sqnum = 1
            elif count in [6,7,8,15,16,17,24,25,26]:
                sqnum = 2
            elif count in [27,28,29,36,37,38,45,46,47]:
                sqnum = 3
            elif count in [30,31,32,39,40,41,48,49,50]:
                sqnum = 4
            elif count in [33,34,35,42,43,44,51,52,53]:
                sqnum = 5
            elif count in [54,55,56,63,64,65,72,73,74]:
                sqnum = 6
            elif count in [57,58,59,66,67,68,75,76,77]:
                sqnum = 7
            elif count in [60,61,62,69,70,71,78,70,80]:
                sqnum = 8
            for j in sq[sqnum]:
                for k in possible:
                    if j == k:
                        possible.remove(k)
            if len(possible) == 1:

                all[count] = possible[0]
                line = ligne(all)
                column = colonne(line)
                sq = carre(all)
                showff(line,(count,possible[0]))
                liste_vides(all, line, column, sq)

            else:
                vi.append([count, possible])
        count+=1
        colnum+=1
        if(colnum == 9):
            colnum = 0
    return vi, all




def ligne(all):
    sousl = list()
    l = list()
    for i in range(9):
        for j in range(9):
            sousl.append(all[(i*9)+j])
        l.append(sousl)
        sousl = list()
    return l




def colonne(line):
    sousc = list()
    c = list()
    for i in range(9):
        for j in range(9):
            sousc.append(line[j][i])
        c.append(sousc)
        sousc= list()
    return c




def carre(all):
    soussquare = list()
    square = list()
    count = 0
    for i in range(3):
        for j in range(9):
            for k in range(3):
                soussquare.append(all[(j*9)+(k+(i*3))])
                count+=1
                if count == 9:
                    square.append(soussquare)
                    soussquare = list()
                    count = 0
        soussquare = list()
    square[1], square[3] = square[3], square[1]
    square[2], square[6] = square[6], square[2]
    square[5], square[7] = square[7], square[5]
    return square
