import euler_solver
from fastapi import FastAPI
import json

app = FastAPI()

def equation(x, y):
    return -y

def equation2(x):
    return x*x

@app.get("/euler")
async def euler(step: float, x1:float, x2:float, y0:float):
    # Crear el solucionador de Euler con un paso de 0.1

    solver = euler_solver.Solver(step)

    # Resolver la ecuación desde x=0 hasta x=2 con y(0) = 1
    solution = solver.euler(x1, x2, y0, equation)

    # Imprimir la solución
    str1 = "Definir la ecuacion diferencial dy/dx = -y "
    str2 = "Crear el solucionador de Euler con un paso de " + str(step) 
    str3 = " Resolver la ecuacion desde x=" + str(x1)
    str4 = " hasta x=" + str(x2) + " con y(0)=" + str(y0) 
    str5 = " La solucion es: "
    str0 = f"{str1} {str2} {str3} {str4} {str5}"

    # Resolver la ecuación desde x=0 hasta x=2 con y(0) = 1
    trap = solver.trapezoidal(x1, x2, equation2)

    # Imprimir la solución
    str2 = "Crear el metodo trapezoidal con un paso de " + str(step)
    str3 = " Integral de f(x) = x^2 desde " + str(x1) 
    str4 = " hasta " + str(x2) + " usando el metodo del trapecio: "
    str1 = f"{str2} {str3} {str4}"

    data = {
        "Euler": str0,
        "Euler result": solution,
        "Metodo trapezoidal": str1,
        "Trap result": trap
    }
    jj = json.dumps(data)

    return jj

