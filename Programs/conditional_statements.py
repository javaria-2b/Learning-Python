# number is even or odd

num = int(input("enter a num: "))

if(num % 2 ==0):
    print("number is even")
else:
    print("number is odd")


# greatest of 3 numbers entered by the user

a = int(input("enter the first num: "))
b = int(input("enter the second num: "))
c = int(input("enter the third num: "))

if(a >= b and a >= c):
    print("A is the greastest number", a)
elif(b >= a and b >= c):
    print("B is the greastest number", b)
else:
    print("C is the greastest number", c)



# check if a number is a multiple of 7 or not

multiple = int(input("enter a num: "))

if(multiple % 7 ==0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")