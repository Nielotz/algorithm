from math import sqrt
class QuadraticFunction:
    a = b = c = None

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self, x: float):
        return x*x*self.a + x*self.b + self.c

    def get_x_of_common_points_with(self, f):
        a = self.a - f.a  # self.a, f.a != 0 and self.a != f.a 
        b = self.b - f.b
        c = self.c - f.c

        delta = b*b - ((a*c) << 2)

        if not (delta > 0) or c == 0:
            return None, None

        sqrt_of_delta = sqrt(delta)

        root1 = (-b - sqrt_of_delta) / (a << 1)  # a != 0
        root2 = (-b + sqrt_of_delta) / (a << 1)  # a != 0
        if root1 < root2:
            return root1, root2
        return root2, root1

    def calculate_intersection_with(self, f):
        #   a = left side of a trapeze
        #   b = right side of a trapeze
        #   step = height of trapeze
        field = 0

        # Increase n_of_trapezes to increase precission
        n_of_trapezes = 2000  # Can't euqal 0 !
        common_x1, common_x2 = self.get_x_of_common_points_with(f)

        if common_x1 is None:
            return 0

        step = abs(common_x1 - common_x2) / n_of_trapezes
        
        x = common_x1 + step * n_of_trapezes

        y1 = self.calculate(x)
        y2 = f.calculate(x)

        a = abs(y1 - y2)

        while n_of_trapezes:
            b = a

            x -= step

            y1 = self.calculate(x)
            y2 = f.calculate(x)

            a = abs(y1 - y2)

            field += (a + b) / 2 * step #   step never equal 0
            
            n_of_trapezes -= 1
           
        return field

#   Number of tests
n = int(input())

while n:
    #   ax^2 + bx + c
    a, b, c = [int(x) for x in input().split()] 
    f1 = QuadraticFunction(a, b, c)
    
    #   ax^2 + bx + c
    a, b, c = [int(x) for x in input().split()] 
    f2 = QuadraticFunction(a, b, c)

    field = f1.calculate_intersection_with(f2)


    print("{:.2f}".format(round(field, 2)))

    n -= 1
