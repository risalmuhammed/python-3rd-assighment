# PYTHON ASSIGNMENT 3: WHILE LOOP, FOR LOOP AND FUNCTION

# 1. WHILE LOOP - NUMBER GUESSING GAME

import random

secret_number = random.randint(1, 10)
attempts = 3
guess_count = 0

print("\n1. NUMBER GUESSING GAME")

while guess_count < attempts:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess between 1 and 10.")
        continue

    guess_count += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
else:
    print("Better luck next time! The correct number was", secret_number)


# 2. FOR LOOP - MULTIPLICATION TABLE GENERATOR

print("\n2. MULTIPLICATION TABLE GENERATOR")

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 3. FUNCTION - BMI CALCULATOR

print("\n3. BMI CALCULATOR")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", round(bmi, 2))
else:
    print("Weight and height must be greater than zero.")