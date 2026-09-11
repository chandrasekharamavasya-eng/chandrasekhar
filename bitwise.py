#bitwise operator
import numbers


import numbers


a=5
b=3
print (a&b)
print (a|b)
print (a^b)
print (a<<b)
print (a>>b)

    #electric city bill calculator
units = int(input("Enter the number of units consumed: "))
rate =6
bill =units*rate
print("Electricity bill: ",bill)

#travel expense calculator
travel =float(input("travel expense:"))
food =float(input("food expense:"))
hotel =float(input("hotel expense:"))
total = travel + food + hotel
print("Total travel expense: ",total)

  #list in python
  #list is an ordered and changeable collection that can be store
marks =[80,90,75,85]
print(marks)

 #accessing elemnts in a list
marks =[80,90,75,85]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

# change elements in a list
marks =[80,90,75]
marks[1]=88
print(marks)

marks =[92,86,79,42,69,56]
marks[1]=88
print(marks)

#add element in a list
marks =[80,90,75]
marks.append(85)
print(marks)
# remove element from a list
marks =[80,90,75]
marks.remove(90)
print(marks)

#insert element in a list
number=[10,20,30]
number.insert(1,15)
print(number)

#extend element
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#clear element
number=[10,20,30]
number.clear()
print(number)

number =[10,20,30,40]
print(number.index(30))

#count element
number =[10,20,20,30,40]
print(number.count(20))

#sort element
number =[40,10,30,20]
number.sort()
print(number)
number.sort(reverse=True)
print(number)

#reverse element
number =[10,20,30,40]
number.reverse()
print(number)

#copy method
a =[1,2,3]
b = a.copy()
print(b)

#numbers
numbers =[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python
#Tuple is a collective of value that is ordered and cannot be changed
student =("Chandra sekhar",98,"python")
print(student[0]) 

#access values in a tuple
student =("Chandra sekhar",21,85.5)
print(student[0])
print(student[1])
print(student[2])

#imutable nature of tuple
student =("Chandra sekhar",21,85.5)
student[1] =22
#this gives an error because tuple is immutable and cannot be changed
#tuples are imutable and cannot be changed after creation

#count
number=(10,20,20,30,20)
print(number.count(20))

#index
number=(10,20,30,40)
print(number.index(30))

#set
numbers ={10,20,30,40}
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and unindexed
numbers ={10,20,30,20,10}
print(numbers)

#why use set?
#suppose students have selected subject
subject = ("python","java","python","Sql","java")
print(subject)

#add values to a set
subject = {"python", "java"}
subject.add("SQL")
print(subject)

#remove values from a set
subject.remove("java")
print(subject)

#sets do not allow duplicative values
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
print( "my-set")

#dictionaries in python