sample_string = 'test string'

print str(sample_string)

# repr() will format output to be better readable for interpreter
print repr(sample_string)

# arrange data as tables with rjust()
for x in range(1,10):
	print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)

print ''

# arange data with format method
for x in range(1,10):
	print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

# more format method examples
print 'simple {} with given {}'.format('fill', 'arguments')
print 'we can {1} {0} of arguments'.format('order', 'change')
print 'we can use {first} {second} as well!'.format(first='keyword', second='arguments');

arguments_dictionary = {'first': 'dictionary', 'second': 'all'}
print 'we can also use {first}, and pass it {second} into format method'.format(**arguments_dictionary)