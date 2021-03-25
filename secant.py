# Root Finding Method
# Open Method
# Secant Method

import numpy as np 


# Define the main Secant Method Function
def secant(x0,x1,es,imax):
    itera = 0
    xr = x0
    ea = es
    while (ea >= es) and (itera < imax):
        xrold = xr
        x0 = x1
        x1 = xrold
        # Secant Method
        xr = (x1 - (((f(x1))*(x0-x1))/ ((f(x0)) - (f(x1)))))
        itera += 1
        if xr != 0:
            # Formula for Approx. % Error
            ea = abs((xr - xrold)/ xr) *100
    return xr


# The function of the equation being examined
def f(x):
    #y = (x**2) -.5
    #y = 0.5*(x**2) + x - 43
    y = 0.5*(x**2) + 13*x - 43
    print("y equals: ",y)
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
    x0 = eval(input("Initial estimate 1: "))
    x1 = eval(input("Initial estimate 2: "))
    es = eval(input("Prescribed Error threshold: "))
    imax = eval(input("Max iteration threshold: "))

    x = secant(x0,x1,es,imax)
    print("The root has been located at: ",x) 


main()