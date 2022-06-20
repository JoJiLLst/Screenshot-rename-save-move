import os
import glob
import datetime
import shutil
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1
dt = str(datetime.datetime.now())
print(dt)
path="D:\\jillzaza\\Coding_area\\Main project work\\Code\\Screenshot and Save with shortkey\\"
for files in glob.glob(path + '*.png'):
    ogname = "D:\jillzaza\Coding_area\Main project work\Code\Screenshot and Save with shortkey\screenshot.png"
    oldnameNotpng = (os.path.splitext(files)[0])
    newname = "Date ="+oldnameNotpng +"Time ="+dt+".png" #name + datetime
    newname_usetorename = ogname+dt+".png" #name + datetime
       
    source = path + "screenshot.png"
    print(source)
    print(type(source))
    destination = path + dt
    arr = list(destination)
    count = 0
    arr = list(destination)
    count = 0
    for i in range(len(arr)):
        if i !=1:
      
        # replace
            if arr[i] == ':':
                arr[i] = '.'
    # print list
    print(arr)
    
            
            
 
    destination = (destination.replace(".", "-"))
    destination = destination + ".png"
    print(destination)
    print(type(destination))
    source1  = listToString(arr)+".png"
    os.rename(source, source1)
source1  = listToString(arr)   
destination1 = "D:\jillzaza\Coding_area\Main project work\Code\Screenshot and Save with shortkey\Storage Image"

