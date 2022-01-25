#Question 1-Miscelleneous
string="Python is a case sensitive language"
print("(a)Length of string=%s" % len(string))
reversed_string=string[::-1]
print("(b)Reverse string=%s" % reversed_string)
new_string=string[10:26]
print("(c)New string=%s" % new_string)
rep_string=string.replace("a case sensitive","object oriented")
print("(d)Replaced string=%s" % rep_string)
index=string.index("a")
print("(e)Index of given substring=%s" % index)
no_space_string=string.replace(" ","")
print("(f)String with no spaces=%s" % no_space_string)

#Qusetion 2-String Formatting
Name="Sanjosh Gahlyan"
SID=21104022
Department="Electrical"
CGPA=9.9
print("Hey,%s Here!"%Name)
print("My SID is %s"%SID)
print("I am from %s department"%Department,"and my CGPA is %s"%CGPA)

#Question 3-Bitwise operations
a=56
b=10
print("(a)a&b=%d" % (a&b))
print("(b)a|b=%d" % (a|b))
print("(c)a^b=%d" % (a^b))
print("(d)Left shift both a and b with 2 bits:a=%d,b=%d" % (a<<2,b<<2))
print("(e)Right shift a with 2 bits and b with 4 bits:a=%d,b=%d" % (a>>2,b>>4))

#Questin 4-Finding greatest number
a=input("Enter first number=")
b=input("Enter second number=")
c=input("Enter third number=")
if(a>=b) and (a>=c):
    greatest=a
elif(b>=a) and (b>=c):
    greatest=b
else:
    greatest=c
print("Greatest of three numbers is=",greatest)     

#Question 5-Finding name in string
a=str(input(("Type the string:")))
if "name" in a:
    print("Yes")
else:
    print("No")

#Question 6-Triangle problem
x=int(input("Enter length of first side="))
y=int(input("Enter length of second side="))
z=int(input("Enter length of third side="))
if (x+y>z and x+z>y and y+z>x):
    print("Yes")
else:
    print("No")
