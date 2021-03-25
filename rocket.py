# This was the example on the first day of classes for Numerical Methods
# A program to determine the height of a rocket as a function of time.
# h = h(t)

import matplotlib.pyplot as plt
import numpy as np


motor_burn_time = eval(input("What is the motor burn duration? "))
accel = eval(input("What is the rocket's vertical acceleration? "))
time_of_interest = float(input("What time would you like to investigate? "))

# Equations of motion to get height and velocity data
def const_1D_accel_model(t,to,ho,vo,a):
    v = vo + (a*(t-to))
    h = ho + (vo*(t-to)) + (0.5*a*((t-to)**2))
    return (h,v)

# Main Height function. Piece-wise function given time
def height(t):
    (h2,v2) = const_1D_accel_model(motor_burn_time,0,0,0,accel)
    if (t>=0) & (t<=motor_burn_time):
        (h,v) = const_1D_accel_model(t,0,0,0,accel)
    elif (t>=motor_burn_time):
        (h,v) = const_1D_accel_model(t,motor_burn_time,h2,v2,-9.8)
        if h < 0:
            h = 0
    else:
        (h,v) = (0.0,0.0)
    return (h,v)

(h,v) = height(time_of_interest)
print("\n\nAt time:",time_of_interest,"\bs, \nThe height of the Rocket is: ",h,"\bm\n\n")

# Write a function to use the Equations of Motion to gather some of the parameters
# needed for the construction of a nice plot
def params_gather(motor_burn_time,accel):
    (hout,vout) = const_1D_accel_model(motor_burn_time,0,0,0,accel)
    t_glide = -vout/-9.8
    h_glide = (vout*t_glide) - (0.5*9.8*(t_glide**2))
    h_tot = hout + h_glide
    t_fall = np.sqrt(2*h_tot/9.8)
    t_toti = motor_burn_time + t_glide + t_fall
    t_tot = t_toti + (t_toti/10)
    return (motor_burn_time,t_toti,t_tot)

# Define Plotter Function
def hvt_plotter(t_s):
    (t_1,t_2,t_3) = t_s
    res = 500
    step = t_3/res
    (t1,t2,t3) = [],[],[]
    (h1,h2,h3) = [],[],[]
    count = 0
    subcount = -1
    for i in range(res):
        if step*i <= t_1:
            t1.append(step*i)
            (hi,vi) = height(t1[i])
            h1.append(hi)
        elif ((step*i) >= t_1) & ((step*i) <= t_2):
            subcount += 1
            t2.append(step*i)
            (hi,vi) = height(t2[subcount])
            h2.append(hi)
        else:
            t3.append(step*i)
            (hi,vi) = height(t3[i-count])
            h3.append(hi)
        count += 1
    plt.plot(t1,h1,color = 'red',label = 'Engine Burn')
    plt.plot(t2,h2,color = 'blue',label = 'Free Glide')
    plt.plot(t3,h3,color = 'black',label = 'Ground Contact')
    plt.title("Rocket Height over Time")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Rocket Height [m]")
    plt.show()

t_s = params_gather(motor_burn_time,accel)
hvt_plotter(t_s)