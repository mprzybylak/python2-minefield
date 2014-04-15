# String concatenation

# works with two literal
greetings = 'Hello, ' 'World'
print greetings

# with string expressions you have to use + operator
hello = 'Hello, '
world = 'World'

# Substrings, Subscript of Strings

lorem_ipsum_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

# String Subscript
print lorem_ipsum_string[0] # first index

# Negative index subscript will start at the end of string 
print lorem_ipsum_string[-16:-6] 

# String substring with silce notation
print lorem_ipsum_string[6:11]

# Default zero as a first parameter in slice notation
print lorem_ipsum_string[:5]

# Default last character index as a second parameter in slice notation
print lorem_ipsum_string[51:]

# Length of string
TenString = '0123456789'
print len(TenString)