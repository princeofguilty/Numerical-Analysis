import math
from math import sqrt, pow, log, exp
ge = input('Function of x : ')
ge = compile(ge, "<string>", "eval")
f = lambda x: eval(ge)

# Implementing Bisection Method
def bisection(x0, x1, e, n):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    Xold = None
    while condition and n != 0:
        x2 = (x0 + x1) / 2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)), end='')
        if (Xold == None):
            print('')
        else:
            print(', error =', abs((x2 - Xold) / x2 * 100), '%')
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        if (x2==0):
            break

        step = step + 1
        condition = abs(f(x2)) > e
        n-=1
        Xold=x2

    print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')
n = int(input('Maximum iterations: '))

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0, x1, e, n)