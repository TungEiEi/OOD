print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
for i in range(n):
    for k in range(n):
        if k<n-i-1:
            print(".",end="")
        elif k==n-i-1:
            print("*",end="")
        else:
            print("+",end="")
    for k in range(n-1):
        if k>=i:
            print(".",end="")
        elif k==i-1:
            print("*",end="")
        else:
            print("+",end="")
    for k in range(n-1):
        if k<n-i-2:
            print(".",end="")
        elif k==n-i-2:
            print("*",end="")
        else:
            print("+",end="")
    for k in range(n-1):
        if k>=i:
            print(".",end="")
        elif k==i-1:
            print("*",end="")
        else:
            print("+",end="")
    print()
for i in range(n*2-2):
    for k in range(n*2-1):
        if k>=i+2:
            print("+",end="")
        elif k==i+1:
            print("*",end="")
        else:
            print(".",end="")
    for k in range(n*2-2):
        if k<n*2-i-4:
            print("+",end="")
        elif k==n*2-i-4:
            print("*",end="")
        else:
            print(".",end="")
    print()