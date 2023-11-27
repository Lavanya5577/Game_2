import random

number=random.randint(1,100)
attempt=1
guess=int(input("Guess the number:"))
  
while(True):
    if (guess>number):
        guess=int(input("Guess another number.The number is too big:"))
        attempt+=1
    elif(guess<number):
        guess=int(input("Guess another number.The number is to less:"))
        attempt+=1
    else:
        print(f"Yess you guessed right!! you guessed the number in {attempt} attempts ")
        break