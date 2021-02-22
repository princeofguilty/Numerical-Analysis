import os

print("1. Bisection\n2. False Position\n3. Secant\n4. Newton\n5. Muller")
x = int(input("Which Method to use: "))

if (x == 1):
    os.system('python bisection.py')
if (x == 2):
    os.system('python false_position.py')
if (x == 3):
    os.system('python secant.py')
if (x == 4):
    os.system('python newton.py')
if (x == 5):
    os.system('python muller.py')

os.system("pause")
