#a. Write a Python program to add member(s) in a set and clear a set.
#20CS007_Khush Bhalodiya
fruits = {'Mango','Banana','Apple'}     #Creating a set
fruits.add('Lime')                      #Adding an item to set
print(fruits)                           #Prints the updated set 
fruits.update(['Orange','Kiwi'])        #Adding multiple items to the set
print(fruits)                           #Prints the updated set 
fruits.clear()                          #Clear the set
print(fruits)                           #Prints the empty set