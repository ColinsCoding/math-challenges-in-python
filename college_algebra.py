from sympy import symbols, Eq, solve

def solve_equation(equation, variable):
    return solve(equation, variable)

def main():
    # Define symbols
    h = symbols('h')
    n = symbols('n')
    k = symbols('k')
    f = symbols('f')

    # List of equations and their variables
    problems = [
        (Eq(1.5 * (2 - 4 * h), 6 * h), h),
        (Eq(((4*n) + 2), 6 * ((( 1/3 * n)) - 2/3)), n),
        (Eq((1/4) * k, 3 * (((-1 / 4) * k) + 3)), k),
        (Eq((4 * (.5 * f - 0.25)), 6 + f), f)
    ]

    # Solve each equation
    for equation, variable in problems:
        solution = solve_equation(equation, variable)
        print(f"The solution for {variable} is: {solution}")

if __name__ == "__main__":
    main()