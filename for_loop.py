for letter in "Eklavya":
    print(letter) #prints all letters in eklavya

friends = ["hello","TATA","Bye Bye"]

for a in friends:
    print(a)

for friend in range(len(friends)): #length is 3, but it iterates from 0 to 2 as iteration starts from 0
    print(friends[friend])

for i in range(3,49):#49 doesnt get included
    print(i)

for index in range(5):
    print(index)


#exponent function

def exponent(a,b):
    result = 1
    for index in range(b):
        result=result*a
    return result

print(exponent(2,6))

print(2**6)# easy to get exponent in python       
    
