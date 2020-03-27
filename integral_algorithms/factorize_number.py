# Without usage of any lib
def factorize(number):
    if number == 1:
        return 1

    factors = []
    i = 2
    while number >= i * i:  # Same as sqrt(number) >= i
        if number % i == 0:
            factors.append(i)
            number //= i
        else:
            i += 1

    if number != 1:
        factors.append(number)

    return factors



[print(i, factorize_faster_faster(i)) for i in range(1, 100)]

