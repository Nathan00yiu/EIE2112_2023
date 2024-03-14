import matplotlib.pyplot as plt
import numpy as np

# define the function
f = lambda x: -3*x**2 + x - 1

# calculated critical point
x_c = 1/6

# choose a domain for x points
x_range = np.linspace(-1,1,100)

# plot the funcion in the chosen domain
plt.plot(x_range, f(x_range), label="f(x)")
# Add a vertical line across the Axes for the critical point
plt.axvline(x_c, linestyle="--", color="k", label="Critical point")
# Show the legned and set the location of the legend
plt.legend(loc="best")
plt.show()
