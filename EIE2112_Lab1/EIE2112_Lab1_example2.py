import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**3 - 2*x**2 + x

x_p = 1
x_n = 1/3

x_range = np.linspace(-0.25,1.5,100)
plt.plot(x_range, f(x_range), label="f(x)")
plt.axvline(x_p, linestyle="--", color="k", label="Critical point +")
plt.axvline(x_n, linestyle="--", color="r", label="Critical point -")
plt.legend(loc="best")
plt.show()