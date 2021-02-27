import os
from pathlib import Path


a = os.path.dirname(os.path.abspath(__file__))

print(Path.cwd())



FileNames = ["file-number-1" +str(i) for i in range (10)]


## this fucntion create a list of .txt file


def Fromlistcretefile(mylist):
    for i in mylist:
        file = open(str(i)+".pdf", "w") 
        file.write("the file name is: " + str(i)) 
        file.close()        

#Fromlistcretefile(FileNames)
