from numpy import *
import matplotlib.pyplot as plt

x = linspace(0, 5, 100)
y = -5*cos(10*x)*sin(3*x)/(x**x)
plt.plot(x, y, 'b-', linewidth=3.0, label='-5*cos(10*x)*sin(3*x)/(x^x)')
plt.axis([0, 5, -7, 7])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('My plot')

plt.show()