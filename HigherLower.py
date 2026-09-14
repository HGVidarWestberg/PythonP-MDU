import subprocess; subprocess.run('cls', shell=True)
import random

number = random.randint(0,99)
print(number)
guesses = 0

while True:
    guess = input("gissa ett tal")
    try:
        guess = int(guess)
    except ValueError:
        print("inte ett tal")
        continue
    if guess == number:
        print(f"du klarade det på {guesses} gissningar")
        break
    elif guess > number:
        print("Lägre")
        guesses += 1
    elif guess < number:
        print("Högre")
        guesses += 1