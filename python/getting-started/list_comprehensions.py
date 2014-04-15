# generate list
# syntax = [ <expression> <for_expression> ]
# for_expression = <for_statement> <if_statment(optional)>
squares_list = [x**2 for x in range(10)]
print str(squares_list)

even_list = [x for x in range(10) if x % 2]
print even_list 

# tuple has to be in parenthesis
tuples = [(x,x*2) for x in range(10)]
print str(tuples)