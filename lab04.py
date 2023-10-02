# Задача 1. Да се напише if-конструкция, която проверява стойността на две целочислени
# променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма
# от втората.

# x = int(input())
# y = int(input())
# if x > y:
#     t = y
#     y = x
#     x = t
#     print({x},{y})
# else:
#     print({x},{y})

# Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа,
# без да го пресмята.

# x = int(input())
# y = int(input())
# if  (x > 0 and y > 0) or (x < 0 and y < 0):
#     print("+")
# elif (x < 0 and y > 0) or (x > 0 and y < 0):
#     print("-")
# else:
#     print("Both numbers are zero")

# Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
# дадени числа.

# x = int(input())
# y = int(input())
# z = int(input())
# if x > y and y > z:
#     print (f"The biggest number is x = {x}")
# elif x < y and y > z:
#     print (f"The biggest number is y = {y}")
# else:
#     print (f"The biggest number is z = {z}")

# Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език.

x = int(input())
0 <= x <= 9
if x == 0:
    print("Нула")
elif x == 1:
    print("Едно")
elif x == 2:
    print("Две")
elif x == 3:
    print("Три")
elif x == 4:
    print("Четири")
    

