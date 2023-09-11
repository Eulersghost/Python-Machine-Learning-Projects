name1=input("What is your name? ")
name2=input("What is there name? ")

#combine both inputs
combine = name1 + name2

#convert the name to lower characters 
t_name = combine.lower()

#switch to counting strings/ints
f = t_name.count('t')
i = t_name.count('r')
r = t_name.count('u')
s = t_name.count('e')

firs = f + i + r + s


t = t_name.count('l')
n = t_name.count('o')
a = t_name.count('v')
m = t_name.count('e')
#e = t_name.count('')

tnam = t + n + a + m 

final_score = int (str(firs) + str(tnam))

if final_score < 10 or final_score > 90:
    print (f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >=40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")