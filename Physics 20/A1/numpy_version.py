import numpy as np, math, sys
from matplotlib import pyplot as plt 

# command line arguments
f_x = 1
f_y = 1.5
A_x = 4
A_y = 5
phi = 1
delta_t = 0.001
N = 10000

t_values = (np.arange(0, N+1).reshape(N+1,1)) * delta_t
X_values = A_x * np.cos(2 * math.pi * f_x * t_values)
Y_values = A_y * np.sin((2 * math.pi * f_y * t_values) + phi)
Z_values = X_values + Y_values

np.savetxt("X_data.txt", np.hstack((t_values, X_values)))
np.savetxt("Y_data.txt", np.hstack((t_values, Y_values)))
np.savetxt("Z_data.txt", np.hstack((t_values, Z_values)))

plt.figure(0)
plt.plot(X_values, Y_values)
plt.xlabel("X ---->")
plt.ylabel("Y ---->")
plt.savefig("deleteME.png")

plt.figure(1)
plt.plot(t_values, Z_values)
plt.xlabel("t ---->")
plt.ylabel("Z(t) ---->")
plt.savefig("beats3.png")
