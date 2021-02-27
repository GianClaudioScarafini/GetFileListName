import os
from pathlib import Path
from os import walk

mypath = os.path.dirname(os.path.abspath(__file__))








## this fucntion create a list of .txt file


def Fromlistcretefile(mylist):
    for i in mylist:
        file = open(str(i)+".pdf", "w") 
        file.write("the file name is: " + str(i)) 
        file.close()        

#Fromlistcretefile(FileNames)

def controlfilename(Mypath,extension):
    f = []
    filterFile = []
    for (dirpath, dirnames, filenames) in walk(Mypath):
      f.extend(filenames)
      break

    for i in f:
        if os.path.splitext(i)[-1] == extension:
            filterFile.append(os.path.splitext(i)[0])

    return filterFile

mypdf = controlfilename(mypath,'.pdf')
print(mypdf)
"""
test_string = 'file1_with_extra_underscores_lead.pdf'
filename = os.path.splitext(test_string)[0]
print(filename)  # 'file1_with_extra_underscores_lead'

test_string_2 = ['thisiaatestfile.txt','thisiaatestfile.txt','file1_with_extra_underscores_lead.pdf','file1_with_extra_underscores_lead.pdf','file1_with_extra_underscores_lead.txt']
#newlist = [os.path.splitext(i) if i[-1] == '.txt' for i in test_string_2 ]

test = []
for i in test_string_2:
    if os.path.splitext(i)[-1] == '.txt':
        test.append(os.path.splitext(i)[0])

"""


