inp_str, pin = input("input number : ").split(",")
pin = int(pin)-1

def checkleft(indexchar,target,str):
    if indexchar < 0 or str[indexchar] != target:
        return 0
    else  :
        return 1 + checkleft(indexchar - 1, target, str)

def checkright (indexchar,target,str):
    if indexchar >= len(str) or str[indexchar] != target:
        return 0
    else  :
        return 1 + checkright(indexchar + 1, target, str)
    
def countgroup(pin=pin):
    left = checkleft(pin-1,inp_str[pin],inp_str) 
    right = checkright(pin+1,inp_str[pin],inp_str) 
    ans =  1 + left + right
    return f"Character : {inp_str[pin]}\nCount : {ans}"
        

if len (inp_str) == 0 :
    print("Output : List is entry")
elif pin > len (inp_str):
    print("Output : Pin number out of range")
elif pin < 1 :
    print("Output : Pin number less than 1")
else:
    print(countgroup())