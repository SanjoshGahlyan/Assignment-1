#Question1-Average of three numbers entered by user

a=input('Enter first number:')
b=input("Enter second number:")
c=input('Enter third number:')
avg=(int(a)+int(b)+int(c))/3
print('The average of three numbers is:',avg)

#Question2-Calculating income tax

a=float(input('Enter the gross income:'))
b=int(input('Enter number of dependents:'))
ti=(a-10000-(3000*b))
tax=(ti)*0.2
print('Income tax in dollars is:',tax)

#Question3-Storing different data type values

SID=21104022
Name='Sanjosh Gahlyan'
Gender='M'
Branch='ELE'
CGPA=10
student_data=[SID,Name,Gender,Branch,CGPA]
print(student_data)

#Question4-Marks of 5 students in sorted manner

m1=int(input("Marks of 1st student:"))
m2=int(input("Marks of 2nd student:"))
m3=int(input("Marks of 3rd student:"))
m4=int(input("Marks of 4th student:"))
m5=int(input("Marks of 5th student:"))

sorted_marks=[m1,m2,m3,m4,m5]
sorted_marks.sort()
print(sorted_marks)

#Question5(a)-Printing a specified list

a=['Red','Green','White','Black','Pink','Yellow']
a.pop(3)
print(a)

#Question5(b)-Removing specific colours and replacing them

a=['Red','Green','White','Black','Pink','Yellow']
del a[3:5]; a.insert(3,'Purple')
print(a)


