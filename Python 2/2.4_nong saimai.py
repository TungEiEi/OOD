def hbd(age):
    if (age % 2 == 0):
        old = 20
    elif (age % 2 == 1):
        old = 21

    return f"saimai is just {old}, in base {age//2}!"

year = input("Enter year : ")

print(hbd(int(year)))