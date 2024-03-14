import matplotlib.pyplot as plt
import numpy as np

# define the funcion
f = lambda x: np.sin(x) + 3*x**2

# define the gradient descent algorithm for this funcion
def find_min_gradient(start_point, step, num_iterations):
    x = start_point
    # create a list to store the change of x
    x_history = [x]
    for i in range(num_iterations):
        # calculted the gradient for this example
        grad_x = np.cos(x) + 6*x
        # update rule
        x = x - step*grad_x
        x_history.append(x) # store each updated x
        # calculted the gradient for the updated x
        new_grad_x = np.cos(x) + 6*x
        # stop criteria: new_grad_x = 0 or new_grad_x changes sign
        if new_grad_x == 0 or new_grad_x*grad_x < 0:
            print("The minimum point at x=", x, "y=", f(x))
            break
    return x_history

x_history = find_min_gradient(start_point=4, step=0.07, num_iterations=100)
x_range = np.linspace(-5,5,100)
plt.plot(x_range, f(x_range), label="f(x)")
# here, we need transfer list to array for x_history
plt.plot(x_history, f(np.array(x_history)), 'rx', label='update x')
plt.legend(loc="best")
plt.show()