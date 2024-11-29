# x=10
#
# def sum():
#     global x
#     x=20
#     x=x+1
#     return x
#
# def sum1():
#     return x+1
#
# print(x)
# print(sum())
# print(sum1())

#
# with open("example.text","w") as myfile:
#     myfile.write("Hello World\n")
#
# with open("example.text", "r") as myfile:
#     content=myfile.read()
#     print(content)


#import os
#os.rename("Module03","Module3")
#os.rename("example.text","new_examble.text")
#os.remove("test/text.text")
#os.remove("test")
#
# import os
# file_list=os.listdir("test")
# print(file_list)

# import zipfile
#
# with zipfile.ZipFile("new.zip","w") as zip:
#     zip.write("test/test-Copy.text")


import csv

# data=[
#     ["Name","Salary","Designation","Department","Location"],
#     ["Alice","70000","Software Engineer","IT","New Yerk"],
#     ["Bob","80000","Software Artechack","IT","Canada"],
#     ["John","90000","System Engineer","IT","Dhaka"]
# ]
#
# with open("new.csv","w") as file:
#     file_witer=csv.writer(file)
#     file_witer.writerows(data)

#
# with open("new.csv","r") as file:
#     file_reader=csv.reader(file)
#     for row in file_reader:
#         print(row)

"""
li=[7,15,17,9]
li[1:3]=[14,48,9]
print(li)

numbers=[5,6,7,8,9,10]
numbers.in
print(numbers[5::7])

"""
"""
temp=5
def func():
    temp=10
    print(temp)
func()
print(temp)"""
"""
li=[2,3]
li2=[4,5]
li.extend(li2)
print(li)"""

def calcu(a,b):
    sum=a+b
    sub=a-b
    return sum, sub
print(calcu(20,1.0))
