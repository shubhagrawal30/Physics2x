import sys, math, matplotlib.pyplot as plt
# command line arguments
f_x = float(sys.argv[1])
f_y = float(sys.argv[2])
A_x = float(sys.argv[3])
A_y = float(sys.argv[4])
phi = float(sys.argv[5])
delta_t = float(sys.argv[6])
N = int(sys.argv[7])

t_values = []
X_values = []
Y_values = []
Z_values = []

for n_value in range(0, N+1, 1):
    t_value=delta_t*n_value
    X_values.append([t_value, A_x * math.cos(2 * math.pi * f_x * t_value)])
    Y_values.append([t_value, A_y * math.sin(2 * math.pi * f_y * t_value + phi)])
    Z_values.append([t_value, (X_values[-1])[1] + (Y_values[-1])[1]])

collection= ["X", "Y", "Z"]
files = {}
for SeqName in collection:
    filename = SeqName + "_data.txt"
    f = open(filename, "w")
    files[SeqName] = f

values = {"X": X_values, "Y": Y_values, "Z": Z_values}

for SeqName in collection:
    for value in values[SeqName]:
        files[SeqName].write(str(value)+"\n")
files[SeqName].close()

plt.plot(X_values)
plt.show()