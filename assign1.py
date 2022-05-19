# # working of try()

try:
    # Floor Division : Gives only Fractional
    x = int(input("Enter the number: "))
    y = int(input("Enter the number: "))
    result = x // y
    print("Yeah ! Your answer is :", result)
    result = x // d

except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")

except NameError:
    print("Name is not defined")

except ValueError:
    print("Please Enter the Integer Value")
else:
    print("Yeah ! Your answer is :", result)
finally:
    print('Program Completed,Nothing to Pending')
