def addition(x, y):
	return x+y

def subtrsction(x, y):
	return x-y

def multiplication(x, y):
	return x*y

def division(x, y):
	if y==0:
		raise ZeroDivisionError('The divisor cannot be zero')
		return x / y