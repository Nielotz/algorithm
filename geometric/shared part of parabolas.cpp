#include <iostream>
#include <cmath>

using namespace std;

struct QuadraticFunction
{
    int32_t a, b, c;
    QuadraticFunction(int32_t a, int32_t b, int32_t c):
    a(a), b(b), c(c) {}

    double calculate(double x) {
        return x * x * this->a + x * this->b + this->c;
    }

    pair<pair<double, double>, bool> get_x_of_common_points_with(QuadraticFunction f) {
        int32_t a = this->a - f.a;
        int32_t b = this->b - f.b;
        int32_t c = this->c - f.c;

        int32_t delta = b * b - 4 * a * c;
        if (!(delta > 0))
            return pair<pair<double, double>, bool>(pair<double, double>(0, 0), false);

        double sqrt_of_delta = sqrt(delta);
        double root1 = (-b - sqrt_of_delta) / (int64_t(2) * a);
        double root2 = (-b + sqrt_of_delta) / (int64_t(2) * a);

        if (root1 < root2)
            return pair<pair<double, double>, bool>(pair<double, double>(root1, root2), true);
        return pair<pair<double, double>, bool>(pair<double, double>(root2, root1), true);
    }

    double calculate_intersection_with(QuadraticFunction f) {
        double field = 0;
        uint64_t n_of_trapezes = 3000;  // Can't euqal 0 !

        pair<pair<double, double>, bool> commons = this->get_x_of_common_points_with(f);
        if (!commons.second)
            return 0;
        pair<double, double> common = commons.first;

        double step = abs(common.first - common.second) / n_of_trapezes;
        double x = common.first + step * n_of_trapezes;
        double y1 = this->calculate(x);
        double y2 = f.calculate(x);
        double a = abs(y1 - y2);
        double b;
        while (n_of_trapezes--) {
            b = a;
            x -= step;

            y1 = this->calculate(x);
            y2 = f.calculate(x);

            a = abs(y1 - y2);

            field += (a + b) / 2 * step; //  step never equal 0
        }
        return field;
    }
};

int main()
{
    uint64_t n;
    cin >> n;
    double result;

    while (n--) {
        int32_t a, b, c;
        cin >> a >> b >> c;
        QuadraticFunction f1(a, b, c);
        cin >> a >> b >> c;
        QuadraticFunction f2(a, b, c);

        result = f1.calculate_intersection_with(f2);

        printf("%.2f\n", float(uint64_t(round(result * 100)) / 100.0));
    }

    


}
