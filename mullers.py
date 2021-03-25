# Root Finding Method
# Open Method
# Muller's Method

import numpy as np 


# Define the main Muller's Method Function
def mullers(x0,x1,x2,es,imax):
    itera = 0
    ea = es
    while (ea >= es) and (itera < imax):
        itera += 1
        # Muller's Method
        h0 = x1-x0
        h1 = x2-x1
        d0 = (f(x1)-f(x0)) / h0
        d1 = (f(x2)-f(x1)) / h1
        a = (d1-d0)/ (h1+h0)
        b = (a*h1) + d1
        c = f(x2)
        rad = np.sqrt((b**2)-(4*a*c))   # could be complex
        if abs(b+rad) > abs(b-rad):
            den = b + rad
        else:
            den = b - rad
        xr = x2 + ((-2*c)/den)
        if xr != 0:
            # Formula for Approx. % Error
            ea = abs((xr - x2)/ xr) *100
        x0 = x1
        x1 = x2
        x2 = xr
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
    x2 = eval(input("Initial estimate 3: "))
    es = eval(input("Prescribed Error threshold: "))
    imax = eval(input("Max iteration threshold: "))

    x = mullers(x0,x1,x2,es,imax)
    print("The root has been located at: ",x) 


main()