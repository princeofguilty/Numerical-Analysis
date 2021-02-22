import math
from math import sqrt, pow, log, exp

ge = input('Function of x : ')
ge = compile(ge, "<string>", "eval")
f = lambda x: eval(ge)

def secant(x0, x1, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    Xold = None
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)), end='')
        if (Xold == None):
            print('')
        else:
            print(', error =', abs((x2 - Xold) / x2 * 100), '%')
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            break

        condition = abs(f(x2)) > e
        Xold = x2
    print('\n Xm: %0.8f' % (x2))


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')
n = int(input('Maximum iterations: '))

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    secant(x0, x1, e, n)
