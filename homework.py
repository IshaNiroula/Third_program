#for taking marks from user and printing its sum#

list=[]
o=input("Enter the first marks: ")
p=input("Enter the second marks: ")
q=input("Enter the third marks: ")
r=input("Enter the fourth marks: ")
s=input("Enter the fifth marks: ")
list.append(o)
list.append(p)
list.append(q)
list.append(r)
list.append(s)
print(list)
print("The sum of given marks is ",int(o)+int(p)+int(q)+int(r)+int(s),".")

#taking the string and counting it#

a=input("What do you wanna write ? \nans: ")
b=input("Which is the letter you want to count ? \nans: ")
print("The number of letter you want to count is ",a.count(b),".")

#getting minimum and maximum value#

list=[]
i=input("Enter the first number: ")
j=input("Enter the second number: ")
k=input("Enter the third number: ")
l=input("Enter the fourth number: ")
m=input("Enter the fifth number: ")
list.append(i)
list.append(j)
list.append(k)
list.append(l)
list.append(m)
print("The maximum number is ",max(list))
print("The minimum number is ",min(list))

#replacing a word#

name="Ciao, sono Isha  Piacere di conoscerla"
print(name.replace("Ciao","Buongiorno"))
print(name.replace("conoscerla","conoscerti"))

#asking a string and replacing it#

ask=input("What do you want to write? \n :: ")
ask2=input("What do you want to change in above string? \n :: ")
ask3=input("what do you want to change the string by? \n :: ")
print(ask.replace(ask2,ask3))

#converting into uppercase#

place=input("Write something: ")
print(place.upper())


