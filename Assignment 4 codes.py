#Question 1-Hanoitower disk problem
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

hanoi(3,'A','C','B')                             #calling funtion for 3 disks
print(" ")

#Question2-Pascal's Triangle
from math import comb
n = int(input("Enter the number of rows you want to print: "))                                          #Asking the user the number of rows he/she wants

#Through Recursion
print("The Pascal's Triangle using recursion:")
def pascaltriangle(num):
    if num == 1:                                                                                        
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                      #Recursive call                                                           
        current_row = [1]                                                                               
        previous_row = result[-1]                                           #Taking the last row from the data of all rows                            
        for i in range(len(previous_row)-1):                                #Loop for adding the values of top 2 numbers for computing current number's value                            
            current_row.append(previous_row[i] + previous_row[i+1])         
        current_row += [1]                                                                              
        result.append(current_row)                                                                      
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                            #This print() adds space before printing each row                            
    for j in i:
        print(j, end =" ")
    print()

#Through Iteration
print("The Pascal's Triangle using iteration:")
for i in range(n):                                                                                      
    print((n-i-1)*" ",end="")                                                                           
    for j in range(n):                                                                                  
        if comb(i,j) != 0:                                                  #Condition to ignore the cases when combination = 0 (when j>i)                           
            print(comb(i,j),end=" ")                                        #This print() prints each element and adds space after printing each value                            
    print()                                                                 #This print() is for changing line for next row                           
print(" ")

#Question 3-
a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

#Question 4-
class Student:                                                                                          #Creating class Student
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created\n")
    def __del__(self):
        print("\nObject destroyed")
name = input("Enter name of student: ").strip()                                                         #Inputting name and roll number from the user
roll_no = int(input("Enter roll number of %s: " % (name)))
student1 = Student(name,roll_no)                                                                        #Creating object
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))     #Printing the assigned values
del student1                                                                                            #Deleting the object
print(" ")

#Question 5-Storing details of employees
class Employee:                                                                                         #Creating class Employee
    def __init__(self,name,salary):        
        self.name = name
        self.salary = salary
    def print_data(self):
        print("Salary of %s is %d rupees" % (self.name,self.salary))
employee1 = Employee("Mehak",40000)                                                                     #Creating instances for different employees
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
print("The current database is:")                                                                       #Printing the initial values
for i in [employee1,employee2,employee3]:
    i.print_data()

print("\n(a)Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")        #Updating salary of Mehak to 70000
employee1.salary = 70000
print(employee1.salary)

print("\n(b)Deleted the record of %s(whose salary is %d)" % (employee3.name,employee3.salary))
del employee3

print("\nThe final database is:")                                                                       #Printing the final values
for i in [employee1,employee2]:
    i.print_data()
print(" ")

#Question6-Frienship test
#inputting a word from the first friend
word = input("Enter the first word: ")

#inputting a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print(" ")

