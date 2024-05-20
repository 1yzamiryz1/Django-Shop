import re


def validate_mobile_number(number):
	pattern = r'^\+989\d{9}$'
	return re.match(pattern, number) is not None


print(validate_mobile_number('+989123456789'))  # True
print(validate_mobile_number('+98123456789'))  # False


def validate_national_code(code):
	pattern = r'^\d{10}$'
	return re.match(pattern, code) is not None


print(validate_national_code('1234567890'))  # True
print(validate_national_code('12345'))  # False


def validate_name(name):
	pattern = r'^[a-zA-Z\u0600-\u06FF\s]+$'
	return re.match(pattern, name) is not None


print(validate_name('Ali'))  # True
print(validate_name('علی'))  # True
print(validate_name('Ali Reza'))  # True
print(validate_name('Ali123'))  # False
print(validate_name('Ali-Reza'))  # False