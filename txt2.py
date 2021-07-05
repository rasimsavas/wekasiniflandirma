import cv2
folder = open("testprocessed.csv","r")
dosya = open("testson.csv","w+")
for x in folder:
    dos=x.split(",")
    if(dos[0][0:18]=="'testprocessed\\cat"):
        dosya.write(dos[0])
        dosya.write(",")
        dosya.write("cat\n")
        continue
    if(dos[0][0:18]=="'testprocessed\\chi"):
        dosya.write(dos[0])
        dosya.write(",")
        dosya.write("chicken\n")
        continue
    if(dos[0][0:18]=="'testprocessed\\hor"):
        dosya.write(dos[0])
        dosya.write(",")
        dosya.write("horse\n")
        continue
folder.close()
dosya.close()
