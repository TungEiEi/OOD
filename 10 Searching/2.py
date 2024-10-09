def search(data, key):
    found = False
    for i in range(0,len(key)):
        for j in range(0,len(data)):
            if data[j] > key[i]:
                print(data[j])
                found = True
                break
            else:
                found = False
        if found == False:
            print("No First Greater Value")
        
data, key = input("Enter Input : ").split("/")
l1 = sorted(list(map(int,data.split())))
l2 = sorted(list(map(int,key.split())))
search(l1,l2)
