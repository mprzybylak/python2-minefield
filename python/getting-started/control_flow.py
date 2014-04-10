
# else clause in while loop will execute when condition is resolved to false - break instruction will not execute else clause
while(int(raw_input("Give me a positive number")) > 0):
	print 'yes, positive'
else:
	print 'error, non-negative'

# else caluse in for loop will execute after all iteration over list - break instruction will not execute else clause
for i in range(10):
	print i
else:
	print 'end of range'

# break statement will 'break' nearest loop
for i in range(10):
	if i > 5:
		print 'break!'
		break
	print i

# continue will go to next iteration
for i in range(10):
	if i % 2 ==0:
		print 'continue!'
		continue
	print i