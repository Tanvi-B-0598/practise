ch= input("Enter any random character:-  ")

def is_uppercase(ch):
    if (ord(ch)>=65 & ord(ch)<=90):
        return True
    

if(ch.islower()):
    print("%c is a lowercase letter" %ch)
elif(ch.isnumeric()):
    print("%c is a digit" %ch)
elif(is_uppercase(ch)):
    print("%c is an uppercase letter" %ch)
else:
    print(ch,"is a special character")

