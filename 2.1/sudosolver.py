#import other files
from func_tab import *
from show import *
from verif import *
import time
start = time.time()

#open in.txt file
f = open("in.txt", 'r')


#all is list that contains every cell, in order from 0 to 80
#line is a list that contians sublists that are lines, same for column and sq (square)
#tout, ligne, colonne, carre and empty mean all, line, column and square in french, those functions make the lists

all = tout(f)
line = ligne(all)
column = colonne(line)
sq = carre(all)
verif_all = verif_line(line) or verif_column(column) or verif_square(sq)
if not verif_all:
    empty, all = liste_vides(all, line, column, sq)[0],liste_vides(all, line, column, sq)[1]
    line = ligne(all)
    column = colonne(line)
    sq = carre(all)
    #backtrack function, is a brute force algorithme, that starts with tries in order all cells and checks for errors, if there are any, it goes back and changes previous steps

    def backtrack(empty):
        index = 0
        n = 1
        while True:
            if n == 10:
                all[empty[index][0]] = "V"
                index= index-1
                n = all[empty[index][0]]+1
            if n in empty[index][1]:
                if n !=10:
                    all[empty[index][0]] = n
                line = ligne(all)
                column = colonne(line)
                sq = carre(all)
                verif_all = verif_line(line) or verif_column(column) or verif_square(sq)
                if verif_all == True:
                    n+=1
                    if n == 10:
                        all[empty[index][0]] = "V"
                        index = index - 1
                        n = all[empty[index][0]]+1
                else:
                    index +=1
                    n = 1
                tt = all
                if index == len(empty):
                    return tt
                show(line)
            elif n == 9 and n not in empty[index][1]:
                all[empty[index][0]] = "V"
                index= index-1
                n = all[empty[index][0]]+1
            else:
                n+=1

    if len(empty) != 0:
        final = backtrack(empty)
    line = ligne(all)
    show(line)
else:
    print("base puzzle contains an error")
end = time.time()
print(end - start)
