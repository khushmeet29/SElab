num1 = float(input("Enter first operand: "))  
operator = input("Enter operator : ")
num2 = float(input("Enter second operand: "))  
if(operator == '+'):
	print(num1 + num2)
if(operator == '-'):
	print(num1 - num2)
if(operator == '*'):
	print(num1 * num2)
if(operator == '/'):
	if(num2 != 0):
		print(num1/num2)
	else:
		print("Error: invalid denominator")
		exit()
