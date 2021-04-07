import os
import shutil

#print(os.system("date"))

#os.mkdir("Devesh")

#print(os.getcwd())

#path = "D:\Devesh 07123.10.2020\Apps"
#isexists = os.path.exists(path)
#print(isexists)

#path = "C:/Users/PC-USER/Desktop/Test.txt"
#extension = os.path.splitext(path)
#print (extension)


#print(os.listdir())

source = "D:/Devesh 03.01.2021/Python/Text.txt"
destination = "D:/Devesh 03.01.2021/Devesh"
dest = shutil.copy(source,destination)
