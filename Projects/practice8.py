list1 = ['1', '2']
list2 = ['3', '4']
column = [list1, list2]

#user = input("Choose which one to call? ")

#define user input for row and column:
user= input ("Type your position:") #any time that input is put in it's 
#anytime that input() is used it's passed in as a string

horizontal = int(user[0]) #catches first part of string
vertical = int(user[1])

#in much the same way with lists we can capture the position of user input, remember that for later
print(horizontal)
print (vertical)

print (column[vertical-1]+column[horizontal-1])