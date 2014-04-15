# loop over sequence both as iterator and with index access
for i, v in enumerate(['a', 'b', 'c']):
	print i, v

# loop over two or more sequences
for a, b in zip(['1', '2', '3'], ['a','b','c']):
	print a, b

# reverse iteration
for a in reversed(range(1,10)):
	print a

# iteration over sorted set (sorted method will create copy)
for a in sorted(set(['orange', 'apple'])):
	print a

# iteration over key and value of dictionary
some_dict = {'a':1, 'b':2, 'c':3}
for k,v in some_dict.iteritems():
	print k, v

# change elements of sequence during iteration - we need to make copy
some_sequence = ['a', 'b', 'c']
for e in some_sequence[:]:
	if e == 'b':
		continue
	print e