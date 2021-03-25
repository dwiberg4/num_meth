# Root Finding Method
# Bracketing Method
# False Position Method

import numpy as np 


# Define the main False Position Method Function
def fals_pos(xl,xu,es,imax):
    itera = 0
    xr = xl 
    ea = es
    while (ea >= es) and (itera < imax):
        xrold = xr
        # False Position Method
        xr = xu - ((f(xu)*(xl-xu))  / (f(xl)- f(xu)))
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
    #y = 2*(x**3) - 7*(x**2) + 2*x - 4
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

    x = fals_pos(xl,xu,es,imax)
    print("The root has been located at: ",x) 


main()
