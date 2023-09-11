row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Place the 'X' in the spot")
#row1.pop(-1)
#row1.pop(0)
#row1.insert(0, 'X')

#row1.append('X')
#prompt = input("Place the X:")

#create functions for the rows.
def r1_1():
    row1.pop(0)
    row1.insert(0,'X')
    #print(row1)
 
def r1_2():
    row1.pop(1)
    row1.insert(1,'X')
    print(row1)

def r1_3():
    row1.pop(2)
    row1.insert(2, 'X')
    print(row1)

def r2_1():
    row2.pop(0)
    row2.insert(0, 'X')
    print(row2)

def r2_2():
    row2.pop(1)
    row2.insert(1, 'X')
    print(row2)

def r2_3():
    row2.pop(2)
    row2.insert(2, 'X')
    print(row2)


def r3_1():
    row3.pop(0)
    row3.insert(0, 'X')
    print(row3)

def r3_2():
    row3.pop(1)
    row3.insert(1, 'X')
    print(row3)

def r3_3():
    row3.pop(2)
    row3.insert(2, 'X')
    print(row3)

#recursively call row functions with column functions. 

def c1 ():
    map[0]
    r1_1()

c1()
