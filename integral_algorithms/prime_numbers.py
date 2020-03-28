def check_is_prime(number):
	if number < 9:
		if number in (2, 3, 5, 7):
			return True
		return False
	
	if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
		return False

	i = 11
	while i * i <= number:  # Equal to sqrt(number) >= i but without any lib
		if number % i == 0:
			return False
		i += 2
		if number % i == 0:
			return False
		i += 4
	return True

