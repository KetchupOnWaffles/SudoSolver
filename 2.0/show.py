#show function logs all attempts on console and in out.txt file
out = open("out.txt", 'w+')
def show(line, move, count):
    if count == 0:
        print(move)
        out.write(str(move))
        out.write("\n")
        count+=1
    li = ""
    for i in line:
        for j in i:
            li += str(j) + " "
        li += "\n"
    print(li)
    print("\n")
    print(str(move))
    out.write(li)
    out.write("\n")
    out.write(str(move))
    out.write("\n")
def showf(line):
    li = ""
    for i in line:
        for j in i:
            li += str(j) + " "
        li += "\n"
    print(li)
    out.write(li)
    out.write("\n")
def showff(line, move):
    print(move)
    li = ""
    for i in line:
        for j in i:
            li += str(j) + " "
        li += "\n"
    print(li)
    out.write(str(move))
    out.write("\n")
    out.write(li)
    out.write("\n")
