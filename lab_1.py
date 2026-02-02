
temp_c = int(input("enter temperature in Celsius"))
temp_f=( temp_c * 9/5 ) + 32  #conversion formula
print("temperature in farenheit is",temp_f)
if temp_c > 25:
    print("go to the beach")
elif temp_c > 15:
    print("go hiking")
else:
    print("stay inside")


import random
num = random.randint(1,10)
count = 0
name = input("what is your name")
print("Hello",name,"guess a number between 1 and 10")
while count < 3:  # defines the amount of guesses and the start of the while loop
    guess = int(input("enter your guess:")) 
    count = count + 1
    if guess == num:
        print(name,"you won!")
    elif guess < num:
        print("too low")
    else:
        print("too high")
if guess != num:  # end of game
    print("game over, the number was",num)


