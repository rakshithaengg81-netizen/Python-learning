def largest(a,b):
    if(a>b):
        return a
    else:
        return b
x=largest(6,8)
print("The largest number is: ",x)

p=int(input("Enter the number:"))
def is_positive(p):
    if p>0:
        return "positive"
    else:
        return "negative"
print("The number you entered is:",is_positive(p))

def calculate(a,b,operation):
    if operation=="add":
        return a+b
    elif operation=="sub":
        return a-b
    elif operation=="mul":
        return a*b
print(calculate(10,5,"add"))
print(calculate(20,10,"sub"))
print(calculate(2,10,"mul"))

