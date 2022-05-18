a= int(input("Enter the number: "))
b= int(input("Enter the number: "))
c= int(input("Enter the number: "))
def ma(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>c:
        return b
    else:
        return c

k = ma(a,b,c)
print(f"Maximum number is: {k}")

