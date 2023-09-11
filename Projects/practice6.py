row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map= [row1,row2,row3]
print (f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

#convert input from string to int

integer_horizontal = int(position[0])
integer_vertical = int(position[1])


#from there add it to the map list 
row = map[integer_vertical -1]

#lastly, add it to the row list
row[integer_horizontal-1] = "X"



# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")