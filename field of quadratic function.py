class QuadraticFunction:
    a = b = c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self, x: float):
        return x*x*a + x*b + c

    def calculate_field(self, n_of_trapezes:int, start: int, end: int):
        #   a = left side of a trapeze
        #   b = right side of a trapeze
        #   step = height of trapeze

        field = 0
        step = (end - start) / n_of_trapezes

        a = abs(self.calculate(start + step * (n_of_trapezes)))

        while n_of_trapezes:
            b = a
            a = abs(self.calculate(start + step * (n_of_trapezes - 1)))
            
            field += (a + b) / 2 * step

            n_of_trapezes -= 1

        return field

#   Number of tests
n = int(input())

while n:
    #   ax^2 + bx + c
    a, b, c = [float(x) for x in input().split()] 
    n_of_trapezes, start, end = [float(x) for x in input().split()]

    f = QuadraticFunction(a, b, c)

    field = f.calculate_field(n_of_trapezes, start, end)

    print("{:.2f}".format(field))

    n -= 1
