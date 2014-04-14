import printer
from other_printer import other_print

import package.test.package_printer
from package.test import other_package_printer
from package.test.yet_another_package_printer import yet_another_package_print

from package.test.all import *

# we need to specify function name with module name
printer.print_some()

# we are not supposed to specify module name if function were imported directly
other_print()

# imported from package we need to specify name with full package name
package.test.package_printer.package_print()

# we can import only module from given package
other_package_printer.other_package_print()

# we can import only function form given package
yet_another_package_print()

# we can import 'all' module using star notation. everything that is defined in __all__ sequence inside __init__.py file will be imported
first.first_print()
second.second_print()