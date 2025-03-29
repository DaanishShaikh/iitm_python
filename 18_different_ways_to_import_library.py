import calendar  # Import the full module

# Calling a function from the module requires the module name as a prefix
print(calendar.calendar(2021))  # Prints the entire calendar of 2021
print(calendar.month(2021, 10))  # Prints the calendar for October 2021

from calendar import *  # Importing all functions from the calendar module

# Functions can be used directly without prefix
print(calendar(2021))  # Prints full calendar
print(month(2021, 10))  # Prints October 2021 calendar

from calendar import month, calendar  # Importing only `month` and `calendar` functions

print(month(2021, 10))  # Prints the calendar of October 2021
print(calendar(2021))  # ❌ ERROR: `calendar` is also the module name, this causes confusion

import calendar as c  # Importing the module with alias `c`

print(c.month(2021, 10))  # Calling functions using alias
print(c.calendar(2021))  # Calling another function with alias

from calendar import month as m  # Importing `month` function with alias `m`

print(m(2021, 10))  # Calling the function using its alias
