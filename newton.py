import sympy
import math
from math import sqrt, pow, log, exp

ge1 = input('Function of x : ')
ge = compile(ge1, "<string>", "eval")
f = lambda x: eval(ge)

s = sympy.parse_expr(ge1, evaluate=False)
g = sympy.diff(s)
x = sympy.Symbol('x')
gk = sympy.lambdify(x, g)


def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if gk(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / gk(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f, error = %0.6f %% ' % (step, x1, f(x1), abs(x1-x0)*100))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
n = int(input('Maximum iterations: '))

# Converting input to float
x0 = float(x0)
e = float(e)

newtonRaphson(x0, e, n)
