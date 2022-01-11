import sympy
import math
from math import sqrt, pow, log, exp, sin, cos, tan
import re

## WARNING
## Don't use POW(x,#)

input_function = input('Function of x : ')
compiled_function = compile(input_function, "<string>", "eval")
######################################
f = lambda x: eval(compiled_function)
######################################

input_function_sympy = sympy.parse_expr(input_function, evaluate=False)
differentiation_function = sympy.diff(input_function_sympy)
tmp = sympy.Symbol('x')
#######################################################
f_dash = sympy.lambdify(tmp, differentiation_function)
#######################################################

def newtonRaphson(x0, e, n):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    iteration = 1
    flag = 1
    condition = True
    while condition:
        if f_dash(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / f_dash(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f, error = %0.6f %% ' % (iteration, x1, f(x1), abs(x1-x0)))
        x0 = x1
        iteration = iteration + 1

        if iteration > n:
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
