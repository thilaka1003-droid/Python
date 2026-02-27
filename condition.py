#odd and even check
x=int(input("Enter number"))
if(x%2==0):
    print("Even")
else:
    print("odd")



 # positive or negative
if(x>0):
    print("positive")
elif(x<0):
    print("negative")
else:
    print("Neutral")


#greatest of three numbers
a, b, c = map(int, input("Enter numbers: ").split())
print("Enter three numbers:", a, b, c)
if(a>b and a>c):
    print("A is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")
    
