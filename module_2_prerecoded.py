"""

 # descriptive name
 # lower case with undersore
 # start with leter or underscore
 # No special character
 #Case Sensetive
 # short but miningful
 # use singular noun
 #contintancy
 # avoid __
"""


# data type
# numeric data type
#String Data type
# Sequence Data Type



# numeric data type
"""age=34
print(age)
marks=85.5
print(type(marks))"""

#String Data type
"""
name="Rabbil Hasan"
print(name)"""

# List data type
# Contain Mixed type data
# Contain Duplicate Value
# Maintain Order , index start with 0
# Mutable data type
"""
city=["Dhaka","Rangpur","Khulna", 333, 3.25,True,"Dhaka"]
letter=["A","B","C", "D","E","F","G","H"]
print(letter[5])"""


# Tuple data type
#Contain Mixed type data
#Contain Duplicate Value
# Maintain Order , index start with 0
# Immutable data type
#city=("Dfhaka","Rangpur","Khulna")
#number=("A","B","C", "D","E","F","G","H")
#number1=("A","B","C", "A","E","S","G",20.2)
#print(number1)


# range data type
#numbers=range(1,10)
#numbers1=range(0,10,2)
#print(*numbers1)

# Boolean Data Type

#type=False
#print(type)

# None Data type
#taka=None
#print(taka)

# Mapping Data type Dictonary

"""persons= {
        'name':'Ashraful Islam',
        'age': "40",
        'district':"Tangail",
        'is_bangladeshi': True
    }

print(persons['name'])"""

# Set
# mutable
# unorder
# avoid duplicate value

"""number={1,2,3,2,3,2,2}
print(number)

# Frogen Set
# immutable
# unorder
# avoid duplicate value
unic_number=({1,2,3,4,3,2,4})
print(unic_number)"""

# String indexing
text="#Hello World "
"""
print(text)

print(text[0])"""

# strting slicing start
#print(text[0:5])

# strting slicing end
#print(text[6:])
# Step slicing

#print(text[6::2])

# String repetation
repetation=text *5
#print(repetation)

# string concatanation
"""string1="Hello"
string2="World"

#combine=string1+ ", "+ string2
combine=",".join([string1,string2])
print(combine)"""


text="Hello World"
"""print("Uppercase ",text.upper())
print("Lowercase ",text.lower())
print("Capitalized ",text.capitalize())
print("Title ",text.title())
print("Swap ",text.swapcase())
print("Replace ",text.replace("World", "Python"))
print("Split", text.split(" "))"""

"""word=["Hello", "world"]
print("Text Join", " ,".join(word))

text1="  Hello World  "
print(text1.strip())
print(text1.lstrip())
print(text1.rstrip())
print(text.startswith("Hello"))
print(text.endswith("Hello"))
print(text.endswith("World"))
print("Find ", text.find("World"))"""



#Number
"""
a=10
b=3
c=5.14
d=4
print("Addition", a+b)
print("Subtraction", a-b)
print("Multiplication", a*b)
print("Division", a/b)
print("Integer Division", a//b)
print("Power 10x10x10", a**b)
print("Modulus ", a%b)
"""


#Type Conversion
"""a=10
b=4.84

print("Convert Int to Float", float(a))
print("Convert Float to Int", int(b))
print("Convert Int to Complex", complex(b))"""

"""import math

print("Print Sqire toot", math.sqrt(100))
print("Print Power", math.pow(10,3))
print('Sin 90 degree= ', math.sin(math.radians(90)))
print('Cos 90 degree= ', math.cos(math.radians(0)))

print("natural log of 10", math.log(10))
print("natural log of 10", math.log10(10))
print("Exponential", math.exp(100))
print("GCD 5,45 is ", math.gcd(5,45))
print("LCM 5,45 is", math.lcm(5,45))
print("Absolute Value of -7.154", math.fabs(+7.154))
print("Floor", math.floor(3.7))
print("Ceiling", math.floor(3.7))
print("PI", math.pi)
print("Elears", math.e)"""

for i in range(3):
    print(i)
x=11
y=3
print(x%y)


