import sys
import getopt


def main(argv):
	"""entry point for script"""

	try:
		opts, args = getopt.getopt(argv, 'a:', ['add='])
		for opt, arg in opts:
			if opt in ("-a", "--add"):
				add_channel(arg)

	except getopt.GetoptError:
		usage()

def add_channel(arg):
	pass

def usage():
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
