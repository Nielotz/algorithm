#include <iostream>
#include <cmath>

using namespace std;

//  Change n_of_trapezes to higher value to increase precission

struct Roots {
    const double FIRST = 0;
    const double SECOND = 0;
    const bool VALID = false;

    Roots(const double FIRST, const double SECOND, const bool VALID)
        :FIRST(FIRST), SECOND(SECOND), VALID(VALID)
    {}

    Roots() {
        // valid = false;
    }
};

struct QuadraticFunction
{
    const int32_t A;
    const int32_t B;
    const int32_t C;

    QuadraticFunction(const int32_t A, const int32_t B, const int32_t C) :
        A(A), B(B), C(C) {}

    double calculate(const double& X) {
        return X * X * this->A + X * this->B + this->C;
    }

    Roots get_x_of_common_points_with(QuadraticFunction& f) {
        const int32_t A = this->A - f.A;
        const int32_t B = this->B - f.B;
        const int32_t C = this->C - f.C;

        const int32_t DELTA = B * B - 4 * A * C;
        if (!(DELTA > 0))
            return Roots(0, 0, false);

        const double SQRT_OF_DELTA = sqrt(DELTA);
        const int64_t TWO_A = int64_t(A) * 2;
        const double ROOT1 = (-B - SQRT_OF_DELTA) / TWO_A;
        const double ROOT2 = (-B + SQRT_OF_DELTA) / TWO_A;

        if (ROOT1 < ROOT2)
            return Roots(ROOT1, ROOT2, true);
        return Roots(ROOT2, ROOT1, true);
    }

    double calculate_intersection_with(QuadraticFunction& f) {
        double field = 0;

        // Can't euqal 0 !
        uint64_t n_of_trapezes = 3000;

        const Roots COMMONS = this->get_x_of_common_points_with(f);
        if (!COMMONS.VALID)
            return 0;

        const double STEP = abs(COMMONS.FIRST - COMMONS.SECOND) / n_of_trapezes;

        double x = COMMONS.FIRST + STEP * n_of_trapezes;

        double y1 = this->calculate(x);
        double y2 = f.calculate(x);

        double a = abs(y1 - y2);
        double b;

        const double TRAPEZE_HEIGHT_DIVIDED_BY_TWO = STEP / 2;

        while (n_of_trapezes--) {
            b = a;
            x -= STEP;

            y1 = this->calculate(x);
            y2 = f.calculate(x);

            a = abs(y1 - y2);

            field += (a + b) * TRAPEZE_HEIGHT_DIVIDED_BY_TWO; //  step never equal 0
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
