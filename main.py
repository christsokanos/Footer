import sys
sys.path.append(".")
from task import Footer

f1 = Footer


while True:
    try:
        x = int(input("Total Pages: "))
    except ValueError as err:
        print('Not a number! Try again!')
        continue
    flag = f1.isValid(x)
    if (flag == False):
        print('Total pages must be positive number!')
    else:
        f1.total_pages = x
        break

while True:
    try:
        x = int(input("Current page: "))
    except ValueError as err:
        print('Not a number! Try again!')
        continue
    flag = f1.isValid(x)
    if (flag == False):
        print('Current page must be positive!')
    else:
        f1.current_page = x
        break

while True:
    try:
        x = int(input("Boundaries: "))
    except ValueError as err:
        print('Not a number! Try again!')
        continue
    flag = f1.isValid(x)
    if (flag == False):
        print('Boundaries number must be positive number!')
    else:
        f1.boundaries = x
        break

while True:
    try:
        x = int(input("Around: "))
    except ValueError as err:
        print('Not a number! Try again!')
        continue
    flag = f1.isValid(x)
    if (flag == False):
        print('Around number must be positive number!')
    else:
        f1.around = x
        break

f1.calc()
print(f1.footerOutput())