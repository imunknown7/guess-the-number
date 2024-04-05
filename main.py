import random
number = random.randrange(1, 10)
i = 0
while i < 3:
    guess = int(input("Guess > "))
    if guess == number:
        print("Correct!")
        break
    else:
        i += 1
        print(f"Incorrect... Try again! Tries : {i}/3")
print("The Number was ", number)
print(f"Tries : {i}/3 ")