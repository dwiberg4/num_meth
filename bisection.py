# Root Finding Method
# Bracketing Method
# Bisection Method

import numpy as np 


# Define the main Bisection Method Function
def bisection(xl,xu,es,imax):
    itera = 0
    xr = xl 
    ea = es
    while (ea >= es) and (itera < imax):
        xrold = xr
        # Bisection Method
        xr = (xl+xu)/2
        itera += 1
        if xr != 0:
            # Formula for Approx. % Error
            ea = abs((xr - xrold)/ xr) *100
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
    return xr


# The function of the equation being examined
def f(x):
    y = 0.5*(x**2) + 13*x - 43
    #y = 3*(x**2) + 11*x - 23
    return y


# Optional Graphing Method
def grapher():
    import matplotlib.pyplot as plt
    l = eval(input("Graph Left bound: "))
    r = eval(input("Graph Right bound: "))
    res = eval(input("Desired Resolution: "))
    step = (r-l)/res
    (x,y,flat) = [],[],[]
    for i in range(res):
        x.append(l+(step*i))
        y.append(f(l+(step*i)))
        flat.append(0)
    plt.plot(x,y,color= 'orange')
    plt.plot(x,flat,color= 'purple')
    plt.show()


# Main interface function
def main():
    graph = str(input("Do you wish to graph the function first? "))
    while graph != 'n':
        grapher()
        graph = str(input("Do you wish to graph again? "))
    xl = eval(input("Lower Bound estimate: "))
    xu = eval(input("Upper Bound estimate: "))
    es = eval(input("Prescribed Error threshold: "))
    imax = eval(input("Max iteration threshold: "))

    x = bisection(xl,xu,es,imax)
    print("The root has been located at: ",x) 


main()
