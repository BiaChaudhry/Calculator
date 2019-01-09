import math
print("                                      >>> CONSOLED BASED CALCULATOR >>>     \n  "                             )
print("This is a consoled Based Calculator , This allowed a user to perform the \n under lying operations:")
print(" >>> Addition \n >>> Subtraction \n >>> Multiplication \n >>> Division \n >>> log \n >>> exponent ")
print("this is also specially designed for the convertion of a number from degree to radian and vice versa")
print("More Over the calculator also allows the user to perform 'TRIGNOMETRIC AND HYPERBOLIC FUNCTIONS' \n like : cos,sin,tan and inverse of all \n also cosh,sinh,tanh and their inverses ")
print("'SO GO ON AND USE IT WELL'")
# CODE FOR CONSOLED BASED CALCULATOR IN PYTHON 3 :
def arthCalculator(num01,num02,operator):
	if operator == "+" :
		print(num01 + num02)

	elif operator == "-":
		print(num01 - num02)

	elif operator == "*":
		print(num01 * num02)

	elif  operator == "/":
		try: 
			result = num01 / num02
		except :
			print("Zero Division Error")
		else:
			print(num01 / num02)

	elif operator == "log":
		num       =      int(input("Enter only one number for applying log:"))
		print(math.log10(num))

	elif operator == "exponent":
		number    =     int(input("Enter only one number for exponent:"))
		print(math.exp(number))


	choice       =      input("Do you Want to perform trignometric and hyperbolic function(Yes or No):")       # CHOOSE YES OR NO FOR GOING INTO TRIGNOMETRIC OR HYPERBOLIC CALCULATIONS


	if choice == "Yes":
		number    =     int(input("Enter one number to perform trignometric and hyperbolic functions:"))
		operator  =     input("Enter any trignometric or hyperbolic function like ; cos , sin , tan etc... :")  # THIS OPERATOR IS ESPECIALLY FOR TRIGNOMETRIC OR HYPERBOLIC CALCULATIONS

		if operator == "cos":
			print(math.cos(number))
		elif operator == "sin":
			print(math.sin(number))
		elif operator == "tan":
			print(math.tan(number))
		elif operator == "acos":
			print(math.acos(number))
		elif operator == "asin":
			print(math.asin(number))
		elif operator == "atan":
			print(math.atan(number))
		elif operator == "cosh":
			print(math.cosh(number))
		elif operator == "sinh":
			print(math.sinh(number))
		elif operator == "tanh":
			print(math.tanh(number))
		elif operator == "acosh":
			print(math.acosh(number))
		elif operator == "asinh":
			print(math.asinh(number))
		elif operator == "atanh":
			print(math.atanh(number))

	else:
		print("Ok")

	convertion         =     input("Do you Want convertioN of any number from degree to radian or vice versa ('yes' or 'no')")
	if convertion == "yes":
		number         =    int(input("Enter a number to convert it from degree to radians or vice versa:"))      # INPUT NUMBER FOR : Convert it from degree to radian or vice versa
		convertionF    =    input("choose convertion:'From radian to degree' or 'From degree to radian' :")       # INPUT CONVERT FROM WHAT TO WHAT


		if convertionF == "From radian to degree":               
			print(math.degrees(number))

		elif convertionF == "From degree to radian":
			print(math.radians(number))
	else:
		print("Ok")



def main():
	num01      = input("Enter a number 01:")
	num02      = input("Enter a number 02:")
	operator   = input("Enter any operator from + , - , * , / , log , exponent :")
	try:
		num01  = int(num01)
		num02  = int(num02)

	except:
		print("Invalid number")
		
	else:
		arthCalculator(num01,num02,operator)
main()





	

