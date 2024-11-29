#Create File
import csv
# with open('batch03.text','w') as myfile:
#     myfile.write("This is test file")

# # read a file
# with open('batch03.text','r') as myfile:
#     content= myfile.read()
#     print(content)


import os
# Rename a File

# os.rename('batch03.text','batch03.docx')

# Dwlete a file
#os.remove("batch03.docx")

# Folder Create

#os.mkdir("Batch03")
#with open("Batch03/class2.docx",'w') as myfile:
 #   myfile.write("This is test file")
#os.remove("Batch03.class2.docx")
#
# os.mkdir("2024")
# os.mkdir("2024/11")
# with open("2024/11/rabbil.png","w") as myfile:
#     myfile.write("")

#rename directory

#os.rename("2024/11", "2024/nov")

#Delete a Directory
#os.remove("2024/nov/rabbil.png")
#os.rmdir("2024/nov")

import shutil
shutil.make_archive("2024_new",'zip','2024')

# How to extract
import zipfile
with zipfile.ZipFile("2024_new.zip",'r') as myfile:
    myfile.extractall()

# how to make csv file
data=[
    ["name","Salary","Designation","Department","Location"],
    ["alice",70000,"Engineer","IT","Canada"],
    ["Vnace",170000,"Softwere Engineer","IT","new york"],
    ["Bob",500000,"Computer Engineer","IT","Brazil"]
]

# with open("employee.csv", mode="w", newline='') as myfile:
#     csvFileWriter=csv.writer(myfile)
#     csvFileWriter.writerow(data)

# How to read a csv file
# import csv
# with open("employee.csv",'r') as myfile:
#     myfileReader=csv.reader(myfile)
#
#     for row in myfileReader:
#         print(row)


try:
    with open("abc.text","r") as myfile:
        context=myfile.read()
        num=10/0-
except Exception as e:
    print(f" Error type is:{e} ")
finally:
    print("Something Went Wrong Please try again latter")