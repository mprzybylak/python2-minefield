# example of usage if statement

input_value = int(raw_input("Give me a number"))

# if statement has ':' at the end
if input_value < 0:
	# code block should be intended
	print "negative"
# elif is shorthand notation for else if, also ':' sign at the end
elif input_value == 0:
	print "zero"
# optional else, also ':' sign at the end
else:
	print "positive"
