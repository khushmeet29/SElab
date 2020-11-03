#I am editing this file on github by adding this comment so that I can perform a pull request
num1 = float(input("Enter first operand: "))  
operator = input("Enter operator : ")
num2 = float(input("Enter second operand: "))  
if(operator == '+'):
	print(num1 + num2)
if(operator == '-'):
	print(num1 - num2)
if(operator == '*'):
	print(num1 * num2) #Corrected the error
if(operator == '/'):
	if(num2 != 0):
		print(num1/num2)
	else:
		print("Error: Denominator can't be zero")#Made a change here for branch b1
		exit()
