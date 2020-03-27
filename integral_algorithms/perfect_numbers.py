# There is no need to test higher than sqrt(number), because:
#     number equal x * y == sqrt(number) * sqrt(number) 
#     By checking all numbers in range <2, sqrt(number)>
#     that check: is number / x == int(y) if so then we know,
#     only that x multiplied by that y equals number.  
#     Checking for x higher than sqrt(number), is like checking;
#         is number / y == int(x) what is same as number / x == int(y)

# Without any lib.
def is_number_perfect(number):
    sum = 1
    i = 2 

    while i * i < number:  # Equal to i < sqrt(number) but without any lib  
        if number % i == 0:
            sum += i + number // i
        i += 1

    # If sqrt of number is int, then add sqrt of number to sum only once
    if i * i == number:
        sum += number
    return sum == number

[print(i) for i in range(1, 10000000) if is_number_perfect_better(i)]