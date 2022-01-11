import math
from math import sqrt, pow, log, exp,  sin, cos, tan

input_function = input('Function of x : ')
input_function = compile(input_function, "<string>", "eval")
f = lambda x: eval(input_function)

# Implementing Bisection Method
def bisection(a, b, e, n):
    iteration = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    Xold = None
    while condition and n != 0:
        x_middle = (a + b) / 2
        print('Iteration-%d, x_middle = %0.6f and f(x_middle) = %0.6f' % (iteration, x_middle, f(x_middle)), end='')
        if (Xold == None):
            print('')
        else:
            print(', error =', abs((x_middle - Xold) / x_middle * 100), '%')

        if f(a) * f(x_middle) < 0: ## if f(a) and f(x_middle) both have same sign then a_new = x_middle, else, b_new = x_middle
            b = x_middle
        else:
            a = x_middle
        
        print(",\tUPDATE : a = %0.6f, b = %0.6f\n" %(a,b))
        if (x_middle==0):
            break

        iteration += 1
        condition = abs(f(x_middle)) > e
        n-=1
        Xold=x_middle

    print('\nRequired Root is : %0.8f' % x_middle)


# Input Section
a = input('First Guess: ')
b = input('Second Guess: ')
e = input('Tolerable Error: ')
n = int(input('Maximum iterations: '))

# Converting input to float
a = float(a)
b = float(b)
e = float(e)

# Checking Correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    print("INPUTS : a = %0.6f, b = %0.6f" %(a,b))
    bisection(a, b, e, n)