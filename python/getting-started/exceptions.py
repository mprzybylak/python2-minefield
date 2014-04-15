
# classic try
try:
	x = 1/0
except ZeroDivisionError:
	print 'wrong!'

# else block will be executed if there is no exception raised
try:
	x = 1
except ZeroDivisionError:
	print 'wrong!'
else:
	print 'nothing wrong'

# clean up actions in finally block - it will be allways executed no matter of exception handling style
try:
	x = 1
except ZeroDivisionError:
	print 'Exception!'
else:
	print 'No exception'
finally:
	print 'Cleanup'

# we can raise our own exception with raise keyword
try:
	# we can add some arguments 
	raise Exception('arg1', 'arg2')
# we can use exception instance inside except block
except Exception as inst:
	# we can get arguments passed to exception
	print inst.args
	# empty raise statement inside except block will re-throw exception

# custom exception class Class
class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

try:
	raise MyError('wow wow')
except MyError as e:
	print e.value


# predefined clean-up actions. Some action can be auto executed with "with" statment e.g. auto-closing file after reading it
with open('file_name') as f:
	for line in f:
		print line