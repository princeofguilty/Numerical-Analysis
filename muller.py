import math
from math import sqrt, pow, log, exp

ge = input('Function of x : ')
ge = compile(ge, "<string>", "eval")
f = lambda x: eval(ge)



def swap_points(x):
    s = []
    s = x
    s.sort()
    f = s[1]
    sn = s[2]
    t = s[0]
    s[0] = f
    s[1] = sn
    s[2] = t
    return s

def Muller(a, b, r, max_steps):
    print("Using Muller's method")
    x = [a,b,r]
    for loopCount in range(max_steps):
        x = swap_points(x)
        y = f(x[0]), f(x[1]), f(x[2])
        h1 = x[1]-x[0]
        h2 = x[0]-x[2]
        lam = h2/h1
        c = y[0]
        a = (lam*y[1] - y[0]*((1.0+lam))+y[2])/(lam*h1**2.0*(1+lam))
        b = (y[1] - y[0] - a*((h1)**2.0))/(h1)
        if b > 0:
            root = x[0] - ((2.0*c)/(b+ (b**2 - 4.0*a*c)**0.5))
        else:
            root = x[0] - ((2.0*c)/(b- (b**2 - 4.0*a*c)**0.5))
        print("a = %.5f b = %.5f c = %.5f root = %.5f " % (a,b,c,root))
        print("Current approximation is %.9f" % root)
        if abs(f(root)) > x[0]:
            x = [x[1],x[0],root]
        else:
            x = [x[2],x[0],root]
        x = swap_points(x)



a = float(input("X0 :"))
b = float(input("X1 :"))
c = float(input("X2 :"))
# tol = float(input("tolerance :"))
MAX_ITERATIONS = int(input("iterations :"))
Muller(a, b, c, MAX_ITERATIONS)
