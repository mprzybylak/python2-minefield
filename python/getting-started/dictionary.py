# only inmutable object can be keys in dictionaries

# construction of dictionary
sample_dictionary = {'a':1, 'b':2, 'c':3}
print str(sample_dictionary)

# construction of dictionary with dict() function from sequence of key:val pairs
other_dictionary = dict([('alpha', 100),('beta', 200),('gamma', 300)]);
print other_dictionary

# change value assined to 'a' key
sample_dictionary['a'] = 1000
print str(sample_dictionary)

# get value of given key
print sample_dictionary['b']

# get keys
print sample_dictionary.keys()

# check if map contains key
print 'a' in sample_dictionary

# dictioanry comprehension
comp_dic = {x:x*2 for x in (2,4,6)}