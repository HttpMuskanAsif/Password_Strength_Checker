import re

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
number = re.search(r"[0-9]", password)
symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = 0

if length:
    score += 1
if uppercase:
    score += 1
if lowercase:
    score += 1
if number:
    score += 1
if symbol:
    score += 1

print("\nPassword Strength")

if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")