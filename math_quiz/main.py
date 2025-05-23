import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve

print('1.: 5')


def equation(x):
    return 4**x + 6**x - 9**x

initial_guess = 1.0
solution = fsolve(equation, initial_guess)[0]

print(f"2.: {solution:.2f}")


sum_value = 0
for n in range(1, 100):
    sum_value += (n+1)**0.5 - n**0.5

print(f"3.: {sum_value:.0f}")


def equation(n):
    return n**(2*n) - 2*n**2 + 1

# Kizárólag pozitív kiindulási értékek
guesses = [0.1, 0.5, 1, 2]
solutions = []
for guess in guesses:
    sol = fsolve(equation, guess)[0]
    if sol > 0 and np.isclose(equation(sol), 0, atol=1e-6):
        solutions.append(sol)

solutions = sorted(set(solutions))

print(f"4.: {solutions[0]:.0f}")


M, T, A = symbols('M T A')

eq1 = Eq(M + A - T, 170)
eq2 = Eq(T + A - M, 130)

solution = solve((eq1, eq2), (M, T, A))

print(f"5.: {solution[A]}")


M, K, E = symbols('M K E')

eq1 = Eq(M + E, 10)
eq2 = Eq(K + E, 20)
eq3 = Eq(K + M, 24)

solution = solve((eq1, eq2, eq3), (M, K, E))
M_value = solution[M]
K_value = solution[K]
E_value = solution[E]

# Összsúly
total_weight = M_value + K_value + E_value

print(f"6.: {total_weight}")


e = symbols('e')
equation = Eq(e, 1/6 + (5/6)*(5/6)*e)
solution = solve(equation, e)

print(f"7.: {solution[0]:.2f}")