# a = input("enter thala ")
# print(a," for a reason 🤩👊🏻")

# a = int(input("entr the 1 number : "))
# b = int(input("enter the 2 number : "))

# print("sum: " ,a+b)
# print("sub: " ,a-b)
# print("mul: " ,a*b)
# print("div: " ,a/b)

name = "Thala for a reason "
print(name[0:4])
# for a in name:
#     print(a)
nm = "harry"
print(nm[-4:-1])

str = "welcome to my channel"
print(len(str))
print(len(str.center(90)))
print(str.center(40))

str1 ="Ds"
print(str1.isalnum())
str1 ="World"
print(str1.istitle())
str1 =" we have To kill Moking Bird.It's danger"
print((str1.title()).center(40))

# marks = int(input("Enter your marks : "))
# if (marks < 35):
#     print("You are fail")
# elif (marks > 35 and marks <=40):
#     print("You are pass credit point :4")
# elif (marks >40 and marks <50):
#     print("you are pass credit point :5")
# elif (marks >50 and marks <60):
#     print("You are pass credit point :6")
# elif (marks >60 and marks <70):
#     print("You are pass credit point :7")
# elif (marks >70 and marks <80):
#     print("You are pass credit point :8")
# elif (marks >80 and marks <90):
#     print("You are pass credit point :9")
# else :
#     print("you are at Outstanding credit point :10")


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# name = "sanket"
# for i in name:
#     print(i)

# colors = ['red','green','white']
# # color = (red,black,blue)
# for i in colors:
#     print(i)
#     for j in i:
#         print(j)

# for i in range(0,20,8):
#     print(i)

i = 5
while (i>=1):
    print(i)
    i=i-1
    
# for i in range(11):
    # print(i)

name = "ramachari"
for i in name:
    print(i)

i = 10
while (i<=20):
    print(i)
    i=i+1

    
# i = int(input("enter the number : "))
# while(i<=35):
#     i=int(input("enter the second number : "))
#     print(i)
# print("am done with the loop")

i=1
while i<=5:
    print("thala")
    i=i+1

for i in range(5):
    print("for a reason")

i=1
while i<=5:
    print("thala " ,end="")
    j=1
    while j<=3:
        print("for a reason ,", end="")
        j=j+1
    i=i+1
    print()

height = 10
bounce_factor = 0.5
while height > 0.1:
    print(f"hight {height}")
    height *=bounce_factor
print("blast off")

a = [1,2,3,4,5,6,7,8]
while a:
    print(a.pop())

count = 0
while True:
    count +=1
    print(f"count is {count}.")
    if count ==10:
        break
print("blast off ")


for i in range(12):
    print(f"5 x {i} = {5*i}")
    if i==10:
        print("skip the iteraton")
        continue


# num = int(input("enter number : "))
# total =0
# while num != 0:
#     total +=num
#     print(f"total sum is {total}")
#     num = int(input("enter the number : "))
# print("you are out")

# i=0
# a="thala for a reason"
# while i<len(a):
#     if a[i]=='z' or a[i]=='q':
#         i+=1
#         continue
#     print("current letter : ",a[i])
    #   i+=1

# food = input("enter the food (q for quite) : ")
# while food != "q":
#     print(f"your food is {food}")
#     food = input("enter the another food you want : ")
# print("bye ")

# num = int(input("enter the number between 1 to 10 : "))
# while num <1 or num >10:
#     print("number is not valid")
#     num = int(input("enter the number between 1 to 10 : "))
# print(f"your number is {num}")
    
# i=1
# while i<12:
#     if i==10:
#         print("skipped the iteration")
#         i+=1
#         continue
#     print(f"5 x {i} = {5*i}")
#     i=i+1
    
def fullname(fname,lname):
    print(f"your name is {fname} {lname}")

fullname("thala","for a reason")

def table(digit):
    for i in range(1,11):
        print(f"{digit} x {i} = {digit *i}")

print(f"{table(15)} x {table(21)}")

# a=int(input("enter the number : "))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

#swappiing two numbers-------------------------------->
x=5
y=10
temp = x
x=y
y=temp
print(f"the value of x is {x}".format(x))
print(f"the value of y is {y}".format(y))

#factorial number------------------------------------------>
# a=int(input("enter number : "))
# b=1
# if a<0:
#     print("not possible for negative numbers")
# else:
#     for i in range(1,a+1):
#         b=(b*i)
#     print(f"the factorial of the given number {a} is : {b}")


#simple calculater using if else------------------------------------->
# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number: "))
# c = input("enter the charecter you want (+,-,*,/):")
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     print(a/b)
# else:
#     print("invalid input")


#simple calculater using match case--------------------------------->
# a=5
# b=5
# op = input("enter the operation you want : ")
# match op:
#     case '+':
#         print(a+b)
#     case _:
#         print("invalid input")

# random number generator-------------------------------------------->
# import random
# print(random.randint(0,9))

# meter to km convertor------------------------------------------------> 
# m=1000
# km = float(input("enter the km : "))
# print(f"converting {km}km to {km*m} meter ")
# m=float(input("enter the meter"))
# print(f"converting {m}meter to {m/1000}km")

#positive negetive checker---------------------------------------------->
# a = input("enter the number you want to check : ")
# if int(a)>0:
#     print("its postive number !")
# elif int(a)==0:
#     print("its zero !")
# elif int(a)<0:
#     print("its negative number !")
# else :
#     print("invalid input !")

# leaf year calculater----------------------------------------------------->
# def leafyear(year):
#     if year%4==0:
#         print("this year is leaf year!!")
#     else:
#         print("this is not leaf year")
# leafyear(2013)

# importing calendedr of month------------------------------------------------>
import calendar
yy=2002
mm=3
# mm=5
print(calendar.month(yy,mm))

num = [2,34,565,233,68878,454,2323,-1,-343456,66777,99987]
print(min(num))


# prime number checker non stop🤩🤩🤩🤩🤩🤩🤩🤩🤩------------------------>
# a=int(input("enter the number (0 for quite the loop): "))
# while  not a==0:
#              a=int(input("enter the number (0 for quite the loop): "))
#              flag=False
#              if a==1:
#               print("nither prime")
#              elif a>1:
#                for i in range(2,a):
#                  if a % i==0:
#                      flag=True
#                      break  
#              if flag:
#                print("non prime")
#              else:
#                print("prime number")

# print("bye")

# prime numbers between range---------------------------------------------->
# a=2
# b=20
# for num in range(a,b+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)    


# fibonacci series------------------------------------------------------------->
# n=int(input("enter the terms : "))
# n1,n2 = 0,1
# count=0
# while count<n:
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth
#     count+=1

a=153
temp=a
sum=0
for i in range(1,a):
   while temp>0:
       # temp=a
       digit = temp%10
       sum+= digit**3
       temp//=10
       # print(arm)
if a==sum:
 print("its arm strong")
else:
    print("not")

#sum of natural numbers----------------------------------------------------->
num=10
sum=0
while num>0:
    sum+=num
    num-=1
print(sum)

print("python is ",end="")
print("life for us")

for i in range(10):
    for j in range(i+1):
        print("*",end="")
    print()
# print("88888888888888888")
for i in range(10,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()

a=5
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("its non prime num")
else:
    print("hey its prime")

def name(**name):
    print("Hello mr",name["fname"],name["mname"],name["lname"])

name(fname="mahendra" ,mname="singh",lname="dhoni")

fruit=["ca","asd","ada"]
print(fruit)
fruit.append("mango")
print(fruit)
fruit[2]='apple'
print(fruit)
fruit.remove("ca")
fruit.insert(1,"cherry")
print(fruit)
print(len(fruit))
fruit.pop()
for f in fruit:
    print(f)
name="abhishek"
result=list(name)
print(result)
fruit.extend(name)
print(fruit)

import time
timestamp=time.strftime('%H')
print(timestamp)
if int(timestamp)<12:
    print("good morning")
elif int(timestamp)>=12:
    print("good afternoon")

def factorial(a):
    count=1
    for i in range(1,a+1):
        count=count*i
    print(count)
factorial(6)

def factoria(n):
    if n==1:
        return 1
    else:
        return  n * factoria(n-1)

faf=(factoria(5))
print(faf)


# python SETSSS ----------------------------------------->
s1 = {"thala",7,"for a reason"}
s2 = {"king ",18,"kohli",7}
s3 = {7}
print(s1.difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.issubset(s2))
print(s1.issuperset(s3))
print(s2.add(17))
s2.remove(7)
s2.discard(17)
item=s2.pop()
print(s2)
print(item)


#python DICTIONARY------------------------------------------->
dict = {
    1:"K L RAHUL",
    7:"M S DHONI",
    18:"VIRAT KOHLI",
    10:"SACHIN",
    17:"A B D"
}
print(dict.items())


#try except handling  -------------------------------------------------->
# a= (input("enter the number : "))
# try:
#     print(int(a)*int(a))
# except :
#     print("invalid input")


a=4
b=5
print(a) if a>b else print(b) 
print(a) if a<b else ""

fruit = ['apple','mango','cherry']
for index ,f in enumerate(fruit,1):
    print(index,f)

#import ------------------------------------------------------------->
import math
result = math.sqrt(9)
print(result)


from math import *
result = sqrt(9) * pi
print(result)

# import math
# print(dir(math))

x=10
def fun():
    global x
    x=5
    print(x)

fun()
print(x)

# f=open('hello.py','r')
# text = f.read()
# print(text)
# f.close()

# f=open("hello.py",'a')
# f.write("HEY THALA FOR A REASON..")
# f.close()

# with open('hello.py','a') as f:
#     f.write("thala  ")

# f=open('hello.py','r')
# text = f.read()
# print(text)
# f.close()

# f=open("python2.py",'r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"maths marks of {i} is : {m1}")
#     print(f"science marks of {i} is : {m2}")
#     print(f"english marks of {i} is : {m3}")
#     # print(line)

# f=open('python2.py','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
#     # f.close()

print("-------------------------------------------------------->")
with open('python2.py','r') as f:
    f.seek(3)
    print(f.seek(3))

    print(f.tell())
    data=f.read(10)
    print(data)

print("lambda functons---------------------------------------------->")
square = lambda x :x*x
print(square(5))

cube = lambda x:x*x*x
print(f"cube  is {cube(3)}")

def cube(x):
    return x*x*x
l=[1,2,3,4,5,6,7,8,9,0]
newl=list(map(cube,l))
print(newl)


# INTRODUCTION TO OOPS---------------------------------------------------------->
# CLASS  AND OBJECTS ===============>
class person:
    name="Thala"
    occupation = "The Best Caption"
    salary = 56
    def info(d):
        print(f"{d.name} is a {d.occupation}")

a=person()
b=person()
b.name ="king kohli"
# print(a.name,a.occupation)
a.info()
b.info()


class person:
    def __init__(self,a,b,c):
        self.id=a #int(input("Enter id : "))
        self.name=b #input("Enter name : ")
        self.salary=c #int(input("Enter salary : "))
    def dispaly(self):
        print("The id is :",self.id)
        print("Thenameis",self.name)
        print(f"salary is {self.salary}")
a=person(52,"Sanket",500000000)
a.dispaly()
# b=person()
# b.dispaly()
# c=person()
# c.dispaly()

class OTTsubscription:
    def __init__(self,id,plan,payment):
        self.id=id
        self.plan=plan
        self.payment=payment
    def subscribe(self):
        print(f"subscriber {self.id} subscribed with {self.plan} plan")

class premiumOTTsubscription(OTTsubscription):
    def __init__(self,id,plan,payment,screen):
        super().__init__(id,plan,payment)
        self.screen=screen
    def maxscreen(self,screen):
        self.screen=screen
        print(f"maximum screen of premium subscription is {self.screen}")

a=premiumOTTsubscription(1,"monthly",2000,5)
a.subscribe()
a.maxscreen(67)

# def creater():
#     list=[]
#     i=1
#     while i<=200:
#         list.append(i)
#         i+=1
#     return list
# print(creater())

def generat():
    i=1
    while i<=200:
        yield i
        i+=1
    return i
print(next(generat()))

#list comprehension is oneLine code--------------------------->
easy =[x**3 for x in range(10) if x%2==0]
print("using list comprehension ",easy)

# append ,extend,add,update---------------------------------------->
x=[1,2,3]
x.append(100)
print(x)

x=[1,2,3]
x.extend([100])
print(x)

x={1,2,3}
x.add(100)
print(x)

x={1,2,3,4,5}
x.update({22,343,100})
print(x)

# import random
# print("Snake--0")
# print("Water--1")
# print("Gun----2")
# user = int(input("Enter 0 for Snake , 1 for Water , 2 for Gun : "))
# a=random.randint(0,2)
# # print(a)
# if a==0 and user==1 or a==1 and user==2 or a==2 and user==0:
#     print(f"you chosen {user} computer choosed {a} --computer win")
#     # elif a==1 and user==2:
#     # print(f"you chosen {user} computer choosed {a} --computer win")
# # elif a==2 and user==0:
#     # print(f"you chosen {user} computer choosed {a} -- compter win")
# elif a==user:
#     print(f"you chosen {user} computer choosed {a} -- Draw")
#     # print("draw")
# else:
#     print(f"you chosen {user} computer choosed {a} -- You win")
#     # print("you win")


class library:
    def __init__(self):
        self.noOfBooks=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.noOfBooks=len(self.books)

    def showdetails(self):
        print(f"The library contains {self.noOfBooks} books")
        for book in self.books:
            print(book)

l1=library()
l1.addbooks("mmk")
l1.addbooks("ArR")
l1.addbooks("RB")
l1.showdetails()

list =[2,4,3,6,67,78,23]
for i in list:
    if i%2==0:
        a=[]
        a.append(i)
        print(a)


# numbers=[1,2,3,4,5,6,7,8,9]
# Sum=(sum(numbers))
# # Sum=sum(numbers.append(numbers))
# print(Sum)


# import math
number=[1,2,3,4,5]
print(len(number))

print(bool(4>6)==False)
print(bin(0b101&0b100|0b011))

list=[1,2,3,4,5,6]
for i in list:
    print(i)
print(10 not in list)

a=1
b=2
a,b=b,a
print(f"a is {a}")
print(f"b is {b}")


# IMPORTING CALENDER------------------------------------------------------------>
import calendar
# year=int(input("Enter year : "))
print(calendar.calendar(2024))


# REVERSING STRING------------------------------------------------------------->
# def reverse(string):
#     reversed=""
#     for i in range(len(string)-1,-1,-1):
#         reversed+=string[i]
#     return reversed
# string=input("Enter string : ")
# reversed=reverse(string)
# print(f"Reverse string is : {reversed}")


# num =int(input("Enter a num : "))
# if num==0:
#     print("1")
# else:
#     num*factorial(num)
# print(factorial(num))

print(factorial(6))

list=[1,2,3,4,5]
list2=[3,54,6]
print((list+list2))
print(list*3)
a=["sanket","d","r","a"]
print(a[-3::-1])


b="sanket"
l=list(b)
print(l)