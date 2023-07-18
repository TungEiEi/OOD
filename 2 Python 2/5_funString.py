class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        pass

    def size(self) :
        return len(self.string)

    def changeSize(self):
        ans = ""
        for str in self.string:
            Ascii = ord(str)
            if (Ascii >= 97 and Ascii <= 122):
                Ascii-=32
                ans += chr(Ascii)
            else:
                Ascii+=32
                ans += chr(Ascii)
        return ans

    def reverse(self):
        ans = ""
        for i in range(1,len(self.string)+1):
            ans += self.string[-i]
        return ans

    def deleteSame(self):
        ans = list(set(self.string))
        ans.sort()
        ans = ''.join(map(str,ans))
        return ans



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())