import matplotlib.pyplot as plt
import numpy as np

#define the derivative funcion
def derivative(f, x):
    delta_x = 1/1000000
    return (f(x+delta_x)-f(x))/delta_x

# define the function
f = lambda x: (np.cos(x))*x**2-x

df = lambda x: -x**2*np.sin(x) + 2*x*np.cos(x) - 1

# define the gradient descent algorithm for this funcion
def find_min_gradient(start_point, step, num_iterations):
    x = start_point
    # create a list to store the change of x
    x_history = [x]
    for i in range(num_iterations):
        #update rule
        grad_x = derivative(f, x)
        x = x - step*grad_x
        x_history.append(x) # store each updated x
        # calculted the gradient for the updated x
        new_grad_x = derivative(f, x)
        # stop criteria: new_gard_x = 0 or new_grad_x change sign
        if new_grad_x == 0 or new_grad_x*grad_x < 0:
            print("The minimum point at x=", round(x,3), "y=", round(f(x),3))
            break
    return x_history

x_history = find_min_gradient(start_point = 1, step = 0.05, num_iterations = 100)
x_range = np.linspace(-0.25, 6, num = 100)
plt.plot(x_range, f(x_range), label="f(x)")
# here, we need transfer list to array for x_history
plt.plot(x_history, f(np.array(x_history)), 'rx', label = 'update x')
plt.legend(loc = "best")
plt.show()