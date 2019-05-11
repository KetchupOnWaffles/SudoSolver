#verif functions verify if a number is repeated more than once in a line, column or square and return True if there is an error

def verif_line(line):
    for i in line:
        count = 1
        count2 = 0
        for j in range(9):
            for k in i:
                if k == count:
                    count2 +=1
            if count2 > 1:
                return True
            count+=1
            count2 = 0
            if count == 10:
                count = 1
    return False


def verif_column(column):
    for i in column:
        count = 1
        count2 = 0
        for j in range(9):
            for k in i:
                if k == count:
                    count2 +=1
            if count2 > 1:
                return True
            count+=1
            count2 = 0
            if count == 10:
                count = 1
    return False


def verif_square(sq):
    for i in sq:
        count = 1
        count2 = 0
        for j in range(9):
            for k in i:
                if k == count:
                    count2 +=1
            if count2 > 1:
                return True
            count+=1
            count2 = 0
            if count == 10:
                count = 1
    return False
