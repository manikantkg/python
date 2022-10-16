"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
----------------------------------

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
  
-----------------------------------

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")



-------------------------------------

Use negative indexing to print the last item in the list.


fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

----------------------------------------

Use the correct method to add multiple items (more_fruits) to the fruits set.


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


--------------------------------------------

Use the get method to print the value of the "model" key of the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


--------------------------------------------

Change the "year" value from 1964 to 2020.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

----------------------------------------------

Add the key/value pair "color" : "red" to the car dictionary.


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

------------------------------------------------

if 5 > 2: print("Yes")
else: print("No")               =>   print("Yes") if 5 > 2 else print("No")

--------------------------------------------------

Print i as long as i is less than 6.


i = 1
while
 i < 6:
   print(i)
  i += 1
--------------------------------------------------
while loop exercise from 69-75 very important
--------------------------------------------------
In the loop, when i is 3, jump directly to the next iteration.


i = 0
while i < 6:
  i += 1
  if i == 3:
    
continue

  print(i)
  
  
-----------------------------------------


Print a message once the condition is false.


i = 1
while i < 6:
  print(i)
  i += 1
else:

  print("i is no longer less than 6")
  
--------------------------------------------

If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?


def my_function(*kids):
  print("The youngest child is " + kids[2])

------------------------------------------------


If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?


def my_function(**kid):
  print("His last name is " + kid["lname"])

----------------------------------------------------

Create an object of MyClass called p1:


class MyClass:
  x = 5

p1=MyClass()

----------------------------------------------------

What is the correct syntax to assign a "init" function to a class?


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

------------------------------------------------------



"""