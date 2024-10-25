from sympy import symbols, Eq, solve

def solve_equation(equation, variable):
    return solve(equation, variable)

def problem_1():
    h = symbols('h')
    equation = Eq(1.5 * (2 - 4 * h), 6 * h)
    solution = solve_equation(equation, h)
    print(f"The solution for h is: {solution}")

def problem_2():
    n = symbols('n')
    equation2 = Eq(((4*n) + 2), 6 * (( 1/3 * n)) - 2/3)
    solution2 = solve_equation(equation2, n)
    print(f"The solution for n is: {solution2}")

def probelm_3():
    x = symbols('x')
    equation3 = Eq(2 * (x + 3), 3 * (x - 2))
    solution3 = solve_equation(equation3, x)
    print(f"The solution for x is: {solution3}")

if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()