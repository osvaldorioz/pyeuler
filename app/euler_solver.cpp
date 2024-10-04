// euler_solver.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
#include <vector>

//g++ -O2 -Wall -shared -std=c++20 -fPIC `python3.10 -m pybind11 --includes` euler_solver.cpp -o euler_solver`python3-config --extension-suffix` -I/path/to/eigen

namespace py = pybind11;

class Solver {
public:
    // Constructor
    Solver(double _step_size) : step_size(_step_size) {}

    // Método que resuelve la EDO dy/dx = f(x, y) desde x0 hasta xf con y(x0) = y0
    std::vector<double> euler(double x0, double xf, double y0, const std::function<double(double, double)>& func) {
        std::vector<double> ys;
        double y = y0;
        ys.push_back(y0);
        for (double x = x0; x < xf; x += step_size) {
            y += step_size * func(x, y);
            ys.push_back(y);
        }
        return ys;
    }

    double trapezoidalIntegrate(double a, double b, std::function<double(double)> func) {
        double integral = 0.0;
        for (double x = a; x < b; x += step_size) {
            integral += 0.5 * step_size * (func(x) + func(x + step_size));
        }
        return integral;
    }

private:
    double step_size;  // Tamaño de paso
};


// Exportar la clase a Python usando pybind11
PYBIND11_MODULE(euler_solver, m) {
    py::class_<Solver>(m, "Solver")
        .def(py::init<double>())  // Constructor
        .def("euler", &Solver::euler)
        .def("trapezoidal", &Solver::trapezoidalIntegrate);  // Método solve
}
