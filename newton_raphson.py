# Root Finding Method
# Open Method
# Newton Raphson Method

import numpy as np 


# Define the main Newton Raphson Method Function
def newt_raph(xo,es,imax):
    itera = 0
    xr = xo
    ea = es
    while (ea >= es) and (itera < imax):
        xrold = xr
        # Newton Raphson Method
        xr = xrold - (f(xrold)/deriv(xrold))
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

# Define Derivative of equation function
# Deriv CANNOT be 0
def deriv(x):
    #y = 2*x
    y = x + 13
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
    xo = eval(input("Initial estimate: "))
    es = eval(input("Prescribed Error threshold: "))
    imax = eval(input("Max iteration threshold: "))

    x = newt_raph(xo,es,imax)
    print("The root has been located at: ",x) 


main()