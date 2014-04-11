# Sets unordered collection with no duplication
fruit = set(['apple', 'orange'])
print fruit

# is set contains element?
print 'orange' in fruit

# mathematical operations
set_a = set(['a', 'b', 'c', 'd'])
set_b = set(['b', 'c', 'e', 'f'])

# elements in set_a but not in set_b
print set_a - set_b

# elements in set_a or in set_b
print set_a | set_b

# elements in set_a and in set_b
print set_a & set_b

# xor in set_a and set_b
print set_a ^ set_b

# set comprehension
com_set = { x for x in 'abcdefggha' if x not in 'g'}
print com_set