
employee_file = open("employees.txt","r") 
#r-read
#w-write
#a-append(add new data, cant change existing data)
#r+ - read and write
print(employee_file.readable())#checks if file is readable

print(employee_file.read())#reads whole file

xyz = open("employees.txt","r")
print(xyz.readline())#reads individial line

abc = open("employees.txt","r")
tuv=abc.readlines()#creates a list of all lines
print(tuv)
print(tuv[1])

abc.close()
xyz.close()
employee_file.close()#to close file
