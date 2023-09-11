# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
for num in student_heights:
    total += num


count = 0
for i in student_heights:
    count += 1

grand_total = round(total / count)
print (grand_total)






#This section is for the second coding challnge: 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

scores_range = 0

for max in student_scores:
    if scores_range == 0: 
        scores_range = max
    elif max > scores_range:
        scores_range = max
   #print(scores_range, max)

print (f"The highest score in the class is: {scores_range}")


#This is the exercise using loops and the range function
even_total = 0

for even in range(0, 101, 2):
    even_total = even + 2

print(even_total)

