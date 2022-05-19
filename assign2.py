num = int(input("Enter the number: "))
for z in range(0,num):
    if z == 5:
        # We found what we are looking for
        print("we found 5")
        break # The else statement will not execute because of the break
else:

    # We failed to find what we were looking for
    print("we failed to find 5")
    z = None

print('z = ', z)