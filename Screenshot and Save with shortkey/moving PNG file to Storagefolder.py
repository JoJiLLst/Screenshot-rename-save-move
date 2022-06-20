#moving file to folder
import shutil
from glob import glob
Namelist = (glob('*.png'))
i = len(Namelist)
print(Namelist)
print(type(Namelist))
print(i)
for x in range(i):
    for y in Namelist:
        source = "D:\\jillzaza\\Coding_area\\Main project work\\Code\\Screenshot and Save with shortkey\\"+y
        destination = "D:\jillzaza\Coding_area\Main project work\Code\Screenshot and Save with shortkey\Storage Image"
        new_path = shutil.move(source, destination)
        print(new_path)