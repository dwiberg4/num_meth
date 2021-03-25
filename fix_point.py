# Root Finding Method
# Open Method
# Fixed Point Method

import numpy as np 


# Define the main Fixed Point Method Function
def fix_point(xo,es,imax):
    itera = 0
    xr = xo
    ea = es
    while (ea >= es) and (itera < imax):
        xrold = xr
        # Fixed Point Method
        xr = xrold + f(xrold)
        itera += 1
        if xr != 0:
            # Formula for Approx. % Error
            ea = abs((xr - xrold)/ xr) *100
    return xr


# The function of the equation being examined
def f(x):
    y = (x**2) -.5
    #y = 0.5*(x**2) + x - 43
    #y = 0.5*(x**2) + 13*x - 43
    print("y equals: ",y)
    return y

# IF KNOWN Define Derivative function
def deriv(x):
    y = 2*x
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
    known = str(input("Is the derivative of the equation KNOWN? "))
    if known == 'y':
        if (-2<deriv(xo)) and (deriv(xo)<0):
            print("The Method will converge!")
        else:
            print("This guess will NOT cause the method to converge.")

    es = eval(input("Prescribed Error threshold: "))
    imax = eval(input("Max iteration threshold: "))

    x = fix_point(xo,es,imax)
    print("The root has been located at: ",x) 


main()