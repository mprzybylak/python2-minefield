# write examples
f = open('file_name', 'w')
print f

f.write('test\n')
f.close()

# read examples
r = open('file_name', 'r')
print r.read()
r.close()

r2 = open('file_name', 'r')
for line in r2:
	print r2.tell()
	print line


import json

print json.dumps([1, 'simple', 'list'])

json_file = open('json_file_name', 'w')
json.dumps([1, 'simple', 'list'], json_file)
json_file.close()

