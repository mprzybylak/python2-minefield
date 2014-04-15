class SimpleClass:
	"""Documentation string"""

	i = 0

	def __init__(self):
		print "constructor"
		self.i = 1

	def f(self):
		return "Hello"

# instance of class
a = SimpleClass()

# method invocation
print a.f()

# attribute access - no private fields
print a.i

# monkey patching - adding attribute on the fly
a.test = '12'

print a.test

# inheritance
class NewClass(SimpleClass):
	def __init__(self):
		# call method from super class
		SimpleClass.__init__(self)
		print 'New constructor'

b = NewClass()
print b.f()

print isinstance(a, SimpleClass)
print issubclass(SimpleClass, NewClass)

# multiple inheritance
class A:
	def a(self):
		print 'a'

class B:
	def b(self):
		print 'b'

class C(A,B):
	pass

c = C()
c.a()
c.b()

# private members - there is no private in python, but there is convention that member with prefix "_" should be considered as implementation details
class PseudoPrivate
	_i = 1 # it is not private but by convention we should not mess with this member outside class

# if we use double underscore - name will be mangled with name of class and name of atribute, but it is still not private member. This convention can help with overriding methods in inherited classes
class MangledClass
	def __mangled(self):
		pass