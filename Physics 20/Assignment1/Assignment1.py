def numpy_version():
    import numpy as np, math, sys
    from matplotlib import pyplot as plt 
    
    # command line arguments
    f_x = float(eval(sys.argv[1]))
    f_y = float(eval(sys.argv[2]))
    A_x = float(eval(sys.argv[3]))
    A_y = float(eval(sys.argv[4]))
    phi = float(eval(sys.argv[5]))
    delta_t = float(eval(sys.argv[6]))
    N = int(sys.argv[7])
    
    # creating numpy arrays for the four kinds of modular data
    t_values = (np.arange(0, N+1).reshape(N+1,1)) * delta_t
    X_values = A_x * np.cos(2 * math.pi * f_x * t_values)
    Y_values = A_y * np.sin((2 * math.pi * f_y * t_values) + phi)
    Z_values = X_values + Y_values
    
    # creating and saving database ASCII files (.txt)
    # databse contains values of time and corresponding values of X/Y/Z
    np.savetxt("X_data.txt", np.hstack((t_values, X_values)))
    np.savetxt("Y_data.txt", np.hstack((t_values, Y_values)))
    np.savetxt("Z_data.txt", np.hstack((t_values, Z_values)))
    
    # X Y curve created as figure 0
    # Saved with filename XY with extension .png
    plt.figure(0)
    plt.plot(X_values, Y_values)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("XY.png")
    
    # Z t curve created as figure 1
    # Saved with filename Zt with extension .png
    plt.figure(1)
    plt.plot(t_values, Z_values)
    plt.xlabel("t")
    plt.ylabel("Z")
    plt.savefig("Zt.png")

def list_version():
    import sys, math, matplotlib.pyplot as plt
    # command line arguments
    f_x = float(eval(sys.argv[1]))
    f_y = float(eval(sys.argv[2]))
    A_x = float(eval(sys.argv[3]))
    A_y = float(eval(sys.argv[4]))
    phi = float(eval(sys.argv[5]))
    delta_t = float(eval(sys.argv[6]))
    N = int(sys.argv[7])
    
    # empty lists for attaching data iteratively
    X_values = []
    Y_values = []
    Z_values = []
    
    # values are added for the range values
    for n_value in range(0, N+1, 1):
        t_value=delta_t*n_value
        X_values.append([t_value, A_x * math.cos(2 * math.pi * f_x * t_value)])
        Y_values.append([t_value, A_y * math.sin(2 * math.pi * f_y * t_value \
                                                 + phi)])
        Z_values.append([t_value, (X_values[-1])[1] + (Y_values[-1])[1]])
    
    # list of all kinds of databses that need to be created
    # allows us to do the process iteratively
    collection= ["X", "Y", "Z"]
    
    # iteratively creates a immutable tuple of all database files
    # allows us to use iteration loops
    files = {}
    for SeqName in collection:
        filename = SeqName + "_data.txt"
        f = open(filename, "w")
        files[SeqName] = f
    
    # dictionary of all database arrays
    values = {"X": X_values, "Y": Y_values, "Z": Z_values}
    
    # writes the values (calculated and stored in arrays) to the files
    for SeqName in collection:
        for value in values[SeqName]:
            files[SeqName].write(str(value)+"\n")
    files[SeqName].close()
    
    # X Y curve created as figure 0
    # Saved with filename XY with extension .png
    plt.figure(0)
    plt.plot(X_values, Y_values)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("XY.png")
    
    # Z t curve created as figure 1
    # Saved with filename Zt with extension .png
    plt.figure(1)
    plt.plot(t_values, Z_values)
    plt.xlabel("t")
    plt.ylabel("Z")
    plt.savefig("Zt.png")
