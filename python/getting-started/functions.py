# simple no arg function
def simple_function():
	print 'Hello, function!'

simple_function()

# simple function with argument
def fib(n):
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b

fib(10)
print ''

# example of using documentation string (so-called docstring)
def other_function():
	"""Simple gibbrish print statement"""
	print 'Hello'

other_function()
print other_function.__doc__

# functions can be assigned to variables
f = simple_function
f()

# return values with return statement
def fib_ret(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

print fib_ret(20)

# default values in function
def default_args_fun(a=1, b=2):
	print a, b

default_args_fun()
default_args_fun(10)
default_args_fun(100, 1000)

# keyword argument notation
# keyword arguments goes after positional arguments
default_args_fun(b=1000)

# *[name] argument contains positional arguments
def positional_arguments(a=1,b=2, *arguments):
	print str(arguments)

positional_arguments(1,2)
positional_arguments(1,2,3,4)


# **[name] argument contains keyword arguments
def keyword_arguments(a,b, **arguments):
	print str(arguments)

keyword_arguments(10,20)
keyword_arguments(10,20, aa=1, bb=2)

# unpacking argument

# When function requires e.g. three arguments, and we have it all in one list (list with 3 elements), we can use "unapck" synatx
def unpack_function(a,b):
	print a,b

args = [1,2]
unpack_function(*args)

# We can unpack key arguments from map as a keyword arguments
args_map = {"a":1, "b":2}
unpack_function(**args_map)