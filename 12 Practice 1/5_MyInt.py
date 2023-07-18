class MyInt:
    def __init__(self,num):
        self.num = num

    def __sub__(self, other):
        num2 = other.num
        if (other.num%2 != 0 and other.num < 0):
            other.num += 1
        return f"{self.num} - {num2} = {round(self.num - other.num/2)}"

    def isPrime(self):
        if self.num < 2:
            return False
        i = 2
        while i*i <= self.num:
            if self.num % i == 0:
                return False
            i += 1
        return True
    
    def showPrime(self):
        ans = ""
        if self.num <= 2:
            ans = "!!!A prime number is a natural number greater than 1"
        for i in range(2,self.num+1):
            num = MyInt(i)
            check = num.isPrime()
            if check == True:
                ans += str(i) + " "
        return f"Prime number between 2 and {self.num} : {ans}"
    
    print(" *** class MyInt ***")
a, b = input("Enter 2 number : ").split()
num1 = MyInt(int(a))
num2 = MyInt(int(b))

print(f"{a} isPrime :",num1.isPrime())
print(f"{b} isPrime :",num2.isPrime())
print(num1.showPrime())
print(num2.showPrime())
print(num1-num2)

