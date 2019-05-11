#these functions in order, create the lists all, line, column and sq lists

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
def liste_vides(all):
    count = 0
    vi = list()
    for i in all:
        if i == "V":
            vi.append(count)
        count+=1
    return vi




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
    return square
