
a= int(input("Enter the number: "))
b= int(input("Enter the number: "))
def ma(a,b):
    ret = a if a>b else b
    return ret
k = ma(a,b)
print(f"Maximum number is: {k}")
