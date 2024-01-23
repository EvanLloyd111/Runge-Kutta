#import the required libaries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function
def dydx(y, x):
    dydx = (np.log(x) - y)
    return dydx

#Runge-Kutta
def rungeKutta(x0, y, h, n):
    #intialize arrays which will be used to print a graphical representation of runge-kutta's calculations
    j = [x0]
    k = [y]
    for i in range(1, n + 1):
        #Apply Runge Kutta Formulas to find next value of y
        k1 = dydx(y, x0)
        k2 = dydx(y + (0.5 * k1 * h), x0 + (0.5 * h))
        k3 = dydx(y + (0.5 * k2 * h), x0 + 0.5 * h)
        k4 = dydx(y + (k3*h), x0 + h)

        # Update next value of y
        y = y + (h/ 6.0) * (k1 + (2 * k2) + (2 * k3) + k4)
        # Update next value of x
        x0 = x0 + h

        j.append(x0)
        k.append(y)

        '''
        commented out program that prints results for every iteration of runge-kutta
        
        print("iteration", i,"k1 =",k1,"k2 =", k2, "k3 =",k3,"k4 =", k4, "y =",y, "x =", x0)
        '''

    plt.plot(j, k, 'y--', linewidth=1, label="Runge-Kutta")
    plt.xlabel('x')
    plt.ylabel('y')

    return y

'''
commented out program that requests user input for specification of runge-kutta

x0 = input("x0 = ")
x0 = float(x0)
y0 = input("y0 =  ")
y0 = float(y0)
h = input("h = ")
h = float(h)
n = input("How many iterations?:  ")
n = int(n)
'''

#shows the graph using runge-kutta
print('The value of y at x is:', rungeKutta(2, 1, 0.3, 1000))
plt.title("Graph using Runge-Kutta")
plt.show()

#plots the graph of dydx using odeint
y0 = 1
x = np.linspace(2, 300, 1000)
y = odeint(dydx, y0, x)
plt.plot(x, y, 'g:', linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph using Odeint")
plt.show()

#plots the graph of using odeint and runge-kutta on the same plot
y0 = 1
x = np.linspace(2, 300, 1000)
y = odeint(dydx, y0, x)
plt.plot(x, y, 'g:', linewidth=5, label="Odient")
plt.xlabel('x')
plt.ylabel('y')
rungeKutta(2, 1, 0.3, 1000)
plt.title("Runge-Kutta & Odeint")
plt.legend()
plt.show()

