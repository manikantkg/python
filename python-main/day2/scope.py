# local scope
def local():
    message = "Hello"
    print(message)
local()

# Global scope

text = "Hello"

def example():
    print(text)

example()
print(text)

# Global key word
count = 0

def result():
    global count
    count +=1
result()
result()
    
print(count)

# Quick Exercise:
# Write a program that:

# Creates a global variable total = 0
# Creates a function add_to_total(amount) that adds amount to total
# Call the function 3 times with different amounts
# Print the final total

total = 0
def add_to_total(amount):
    global total
    total +=amount

add_to_total(100)
add_to_total(200)
add_to_total(300)
print(total)

add_to_total(200)