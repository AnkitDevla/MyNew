# working of try()
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))

def divide(x, y):
	try:
		# Floor Division : Gives only Fractional
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
	finally:    
		print('Program Completed')

divide(x,y)
