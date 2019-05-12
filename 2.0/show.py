#show function logs all attempts on console and in out.txt file
out = open("out.txt", 'w+')
def show(line):
    li = ""
    for i in line:
        for j in i:
            li += str(j) + " "
        li += "\n"
    print(li)
    out.write(li)
    out.write("\n")
