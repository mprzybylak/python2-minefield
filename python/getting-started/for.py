
# Regular for notation acts as an interator
words = ['first', 'second', 'third']
print 'Regular loop over list: ' + str(words)
for w in words:
	print w

# If we want to modify list inside for - it is best to create copy of list
list_to_modify = ['1', '22', '333']
print 'example of modifiaction list in loop: ' + str(list_to_modify)
for m in list_to_modify:
	print m

for m in list_to_modify[:]:
	if len(m) > 1:
		list_to_modify.insert(0, m)

print 'modified list: ' + str(list_to_modify)
for m in list_to_modify:
	print m

# We can simulate java-like for with range fuction
print 'range(10) = ' + str(range(10))
print 'range(5,10) = ' + str(range(5,10))
print 'range(0,10,2) = ' + str(range(0,10,2))

print 'for v in range(10)'
for v in range(10):
	print v

print 'for v in range(5,10)'
for v in range(5,10):
	print v

print 'for v in range(0,10,2)'
for v in range(0,10,2):
	print v

# iterate over array with intexes idiom
some_list = ['first', 'second', 'third']
print 'interate over array with indexes. List = ' + str(some_list)
print 'for i in range(len(some_list)):'
for i in range(len(some_list)):
	print i, some_list[i]