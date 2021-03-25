# Program to run Newton Interpolation to specified polynomial degree

import numpy as np 
import matplotlib.pyplot as plt 
import json
import pandas as pd 



# Create the Newton Interpolation 'fdd' Method
def newtInt(x,y):
    fdd = np.zeros((len(x),len(x)))
    print('the fdd array is: \n',fdd)
    for i in range(len(x)):
        fdd[i][0] = y[i]
    for j in range(1,len(x)):
        for i in range(len(x)-(j)):
            print('\n(',j,') and (',i,')')
            fdd[i][j] = ((fdd[i+1][j-1]-fdd[i][j-1])/(x[i+j]-x[i]))
    print(fdd)
    return fdd
       

# Create the Newton Interpolation 'y_eval' Method
def yval(x,fdd,x_eval):
    xtemp = 1
    y_eval = fdd[0][0]
    for m in range(1,len(x)):
        xtemp = xtemp * (x_eval- (x[m-1]))
        y_eval = y_eval + (fdd[0][m] *xtemp)
    return y_eval


# Internal data Function
def routine_Internal():
    #x = [1,4,6,5]
    #y = [7,52,112,79]
    #x = [0,4,11,18,22]
    #y = [0,3,2.5,1,0]
    #x = [0,.0001,.00342,.01072,.02185,.03668,.05506,.07682,.10175]
    #y = [0,.00239,.01552,.02949,.04371,.05773,.07116,.0836,.09455]
    #x = [0,2,5,8,10,13]
    #y = [0,4,28.75,76,120,204.75]
    x = [0,1,3,5,8,12,21]
    y = [0,3,6,8,10,11,12]
    return (x,y)
    

# External Data Function
def routine_External():
    filename = 'Eppler_data_TOP.xlsx'
    path = '/home/dallin/Documents/Horizon/Geometry+Design/'
    fullpath = path + filename

    df = pd.read_excel(fullpath)
    arr = df.to_numpy()
    x = []
    y = []
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if j == 0:
                x.append(arr[i][j])
            else:
                y.append(arr[i][j])
    return (x,y)


# Create the Plotter Function
def plotter(x_points,y_points,x,y):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #ax.set_aspect('equal')

    plt.plot(x_points,y_points, label = 'Interp line',color = 'blue')
    plt.scatter(x,y,color = 'red')
    plt.show()


# Main Routine
def main():
    data = str(input("Internal or External Data? "))
    if data == 'i':
        (x,y) = routine_Internal()
    else:
        (x,y) = routine_External()
    fdd = newtInt(x,y)
    res = 1000
    x_points = []
    y_points = []
    step = (x[len(x)-1] - x[0]) /res
    for i in range(res+1):
        x_points.append(x[0]+(step*i))
    for i in range(len(x_points)):
        y_points.append(yval(x,fdd,x_points[i]))
    plotter(x_points,y_points,x,y)


main()
    
