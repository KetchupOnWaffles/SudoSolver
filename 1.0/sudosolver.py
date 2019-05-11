#import other files
from func_tab import *
from show import show
from verif import *


#open in.txt file
f = open("in.txt", 'r')


#all is list that contains every cell, in order from 0 to 80
#line is a list that contians sublists that are lines, same for column and sq (square)
#tout, ligne, colonne, carre and empty mean all, line, column and square in french, those functions make the lists

all = tout(f)
line = ligne(all)
column = colonne(line)
sq = carre(all)
empty = liste_vides(all)


#backtrack function, is a brute force algorithme, that starts with tries in order all cells and checks for errors, if there are any, it goes back and changes previous steps

def backtrack(empty, verif_all):
    index = 0
    n = 1
    while True:
        if n == 10:
            all[empty[index]] = "V"
            index= index-1
            n = all[empty[index]]+1
        if n !=10:
            all[empty[index]] = n
        line = ligne(all)
        column = colonne(line)
        sq = carre(all)
        verif_all = verif_line(line) or verif_column(column) or verif_square(sq)
        if verif_all == True:
            n+=1
            if n == 10:
                all[empty[index]] = "V"
                index = index - 1
                print ((all[empty[index-1]], empty[index-1], index-1))
                n = all[empty[index]]+1
        else:
            index +=1
            n = 1
        show(line)
        tt = all
        if index == len(empty):
            return tt
verif_all = verif_line(line) or verif_column(column) or verif_square(sq)

final = backtrack(empty, verif_all)
