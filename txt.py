folder = open("test.txt","r")
new = open("test.csv","w+")
for x in folder:
    new.write(x[39:].strip())
    new.write(",")
    new.write(x[40:43])
    new.write("\n")
new.close()
folder.close()
