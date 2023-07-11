print("*** multiplication or sum ***")
a, b = input("Enter num1 num2 : ").split()
num1 = int(a)
num2 = int(b)
if (num1*num2 > 1000):
    print("The result is",num1 + num2) 
else:
    print("The result is",num1 * num2) 