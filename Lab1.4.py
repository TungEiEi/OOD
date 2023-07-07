def rectangle(x1, y1, x2, y2):
    if (y1 > 0):
        print(" "*y1)
    for column in range(y1, y2):
        print(" "*x1,end="")
        for row in range(x1, x2):
            if (column == row):
                print("-",end="")
            else:
                print("*",end="")

        print()

rectangle(1,1,6,6)
rectangle(10,0,16,6)
print("*** Fun with Drawing ***")
# a = input("Enter input : ")