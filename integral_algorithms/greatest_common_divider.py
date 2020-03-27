#  Watch out when using functions with "req" in name. 
#  Default max recursion limit is 997.
#  When built in recursion counter reach 998 - it raises RecursionError.
#  To change max recursion limit use sys.setrecursionlimit(limit).
#  If you don't have to - don't use reqursive to calculate GCD, 
#  it's just not efficient in time and memory consumption.

#  Slow way of calculating GCD
def GCD_sub(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

#  Slow and high memory consumption of calculating GCD
def GCD_sub_req(a: int, b: int):
    if a != b:
        if a > b:
            return GCD_sub_req(a - b, b)
        else:
            return GCD_sub_req(b - a, a)
    return a

#  Fastest, shortest and low memory usage solution way to calculate GCD
def GCD_modulo(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

#  Better than GCD_sub_req but still
def GCD_modulo_req(a: int, b: int):
    if b != 0:
        return GCD_modulo_req(b, a % b)
    return a


