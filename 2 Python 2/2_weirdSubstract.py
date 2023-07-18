def weirdSubtract(n,k):
    ans = n
    while (k!=0):
        ans = str(ans)
        # print(ans[-1])
        if (ans[-1] == "0"):
            ans = ans[:len(ans)-1]
            if (ans == ""):
                ans = 0
            k-=1
            # print("u")
        else:
            ans = int(ans)-1
            k-=1
            # print("d")
    return ans

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))
