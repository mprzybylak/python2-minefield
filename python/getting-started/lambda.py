# lambda function
def summator_fun(a,b):
	return lambda a,b: a+b

# returns function
summator = summator_fun(1,2)
print summator(1,2)
