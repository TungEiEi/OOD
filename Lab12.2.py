print(" *** Rank score ***")
Input = list(map(str,input("Enter ID and Score end with ID : ").split()))
ID = input()
new = {}
for id in range(0,len(Input),2):
    new[Input[id]] = float(Input[id+1])
print(new)