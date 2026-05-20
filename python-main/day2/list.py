fruits = ["mango", "banana", "orange"]


fruits.append("pine apple")
fruits.insert(3,"grapes")
fruits.remove("mango")
fruits.pop()
print(len(fruits))

print(fruits)

numbers = [123, 234, 345, 456]
print(numbers)

for number in numbers:
    print(number)

# Quick Exercise:
# Write a program that:

# Creates a list of 5 programming languages
# Add a new language at the end
# Remove the second language
# Print the list in reverse order
# Loop through the list and print each language

languages = ["C", "C++", "Java", "GO", "Python"]
print(languages)
languages.append("pyspark")
print(languages)
languages.remove("C++")
print(languages)
print(languages[::-1])
for lang in languages:
    print(lang)
