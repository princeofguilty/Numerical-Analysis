import math
from math import sqrt, pow, log, exp, sin, cos, tan

input_function = input('Function of x : ')
input_function = compile(input_function, "<string>", "eval")
f = lambda x: eval(input_function)

def secant(a, b, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    iteration = 1
    condition = True
    Xold = None
    while condition:
        if f(a) == f(b):
            print('Divide by zero error!')
            break
        
        p2 = a - (b - a) * f(a) / (f(b) - f(a))
        print("USING : P0 = %0.6f, P1=%0.6f" %(a, b))
        print('Iteration-%d, p2 = %0.6f and f(p2) = %0.6f' % (iteration, p2, f(p2)), end='')
        if (Xold == None):
            print('')
        else:
            print(', error =', abs((p2 - Xold) / p2 * 100), '%')
        a = b
        b = p2
        iteration = iteration + 1

        if iteration > N:
            break
        
        print() ##newline
        condition = abs(f(p2)) > e
        Xold = p2
    print('\n point: %0.8f' % (p2))


# Input Section
a = input('First Guess: ')
b = input('Second Guess: ')
e = input('Tolerable Error: ')
n = int(input('Maximum iterations: '))

# Converting input to float
a = float(a)
b = float(b)
e = float(e)

# if f(x0) * f(x1) > 0.0:
#     print('Given guess values do not bracket the root.')
#     print('Try Again with different guess values.')
# else:
#     print("INPUTS : a = %0.6f, b = %0.6f" %(a,b))
#     secant(x0, x1, e, n)

print("INPUTS : a = %0.6f, b = %0.6f" %(a,b))
secant(a, b, e, n)
