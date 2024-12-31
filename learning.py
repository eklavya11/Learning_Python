character_name = "John"#variable

print(character_name+" "+"hello")#concatenation
age = 93.94
is_male = True #boolean

print("hello\neklavya")#\n moves text to new line
print("hello\"eklavya")#using\to print"


#working with strings
phrase = "Giraffe Academy"
print(phrase.lower()) #lowercase
print(phrase.upper()) #uppercase
print(phrase.isupper()) #checkuppercase
print(phrase.islower()) #checklowercase
print(phrase.upper().isupper())

print(len(phrase))#length
print(phrase[0])#index0character
print(phrase.index("G"))#indexofG
print(phrase.index("ffe"))#indexof_ffe

print(phrase.replace("Giraffe","Dinosaur"))

#working with numbers

print(2)
print(2.3939)
print(-2929)
print(2+5)

print(38*3)

print(10%3) #gives remainder

my_num = 34
print(str(my_num)+" is good") #converts string to number

xyz=-45
print(abs(xyz))#absolute value
print(pow(2,2))#2 to power of 6
print(max(-34,34))#max
print(round(3.2))#rounding gives 3
print(round(3.7))#gives 4

from math import * #importing to use math module functions

print(floor(3.7))#its a math function
print(ceil(4.5))
print(sqrt(64))

#taking user input

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello "+name+" your age is "+age)

#calculator
num1 = input("Enter first Number: ")
num2 = input("Enter second number: ")
#converting string to int
print("Sum of these numbers is "+str(int(num1)+int(num2)))
#if input is decimal like 4.5
#print("Sum of these numbers is "+str(float(num1)+float(num2)))



