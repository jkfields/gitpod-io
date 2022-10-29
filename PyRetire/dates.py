from dateutil import parser

# initializing string
test_str = "2022-10-29"

# printing original string
print("The original string is : " + str(test_str))

# initializing format
format = "%d-%m-%Y"

# checking if format matches the date
res = True

# using try-except to check for truth value
try:
	res = bool(parser.parse(test_str))
except ValueError:
	res = False

# printing result
print("Does date match format? : " + str(res))