friends = ["kevin","karen","jim","Oscsr","Toby","Chris"]
lucky_numbers = [2,3,5,2,6,4]
print(friends)
print(friends[0])
print(friends[-1]) #first element at last
print(friends[1:])#all elements starting from index 1
print(friends[1:3])#elements from index 1 to 2, doesnt include 3
print(friends[1])
friends[1] = "eklavya"
print(friends[1])
print(friends)


#list_functions
friends.extend(lucky_numbers) #adds another list to the list
print(friends)
friends.append("Rohit") #adds new element to end
print(friends)
friends.insert(1,"Virat")#adds new element to index 1 and pushes all elements to right
print(friends)
friends.remove("jim")
print(friends)
friends.pop()#removes last element in list
print(friends)
print(friends.index("eklavya"))#gives index of the element
print(friends.count("Virat"))#gives count of this element in list 

cricketers = ["Kohli","Virat","Rohit","Ashwin","Bumrah"]
cricketers.sort() #sorts the list
print(cricketers)
cricketers.reverse() #reverses order in list
print(cricketers)

Indian_Crickters = cricketers.copy()# copies a list into another list
print(Indian_Crickters)