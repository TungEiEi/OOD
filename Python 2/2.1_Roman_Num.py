Roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
Number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
class translator:
    def deciToRoman(self, num):
        ans = ""
        for i in range(13):
            count = num // Number[i]
            num %= Number[i]
            ans += count*Roman[i]
            
        return ans

    def romanToDeci(self, s):
        ans = 0
        for str in s:
            for i in range(13):
                if (str == Roman[i]):
                    ans += Number[i]
        
        return ans

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))