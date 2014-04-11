import printer
from other_printer import other_print
import package.test.package_printer

# we need to specify function name with module name
printer.print_some()

# we are not supposed to specify module name if function were imported directly
other_print()

# import from package
package_printer.package_print()