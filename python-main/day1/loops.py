for i in range(5):
    print (i)

# Quick Exercise:
# Write a program that:

# Prints numbers 1 to 10 using a for loop
# Prints only even numbers from 1 to 10 using continue
# Prints numbers using a while loop but stops at 7 using break

for i in range(1,11):
    print (i)
    
    
for i in range(1,11): 
    if i%2 !=0 :
        continue
    print(i)

count = 1
while count < 11: 
    if count == 7:
        break
    print(count)
    count +=1
