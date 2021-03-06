def factorize(number):
    if number == 1:
        return 1

    factors = []
    i = 2
    while i * i <= number :  # Same as sqrt(number) >= i but no need for lib.
        if number % i == 0:
            factors.append(i)
            number //= i
        else:
            i += 1

    if number != 1:
        factors.append(number)

    return factors
