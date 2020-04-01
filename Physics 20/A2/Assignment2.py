import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as sc
def trapezoid(f, a, b, N):
    h = (eval(str(b)) - eval(str(a))) * 1.0 / eval(str(N))
    x = np.linspace(a, b, num=N+1)
    x = f(x) * h * 1.0
    I = np.sum(x) - ((f(a) + f(b))* h / 2.0)
    return I

def simpson(f, a, b, N):
    h = (eval(str(b)) - eval(str(a))) * 1.0 / eval(str(N))
    x = np.linspace(a, b, num=2*N+1)
    x = f(x) * h / 6.0
    x[1:2*N:2] *= 4
    x[2:2*N:2] *= 2
    return np.sum(x)

def plot(f, N_min, N_max):
    N = np.arange(N_min, N_max, 1)
    I = []
    # F and value are changed as per model
    F = np.exp
    value = np.e - 1
    for n in N:
        I.append(np.abs(f(F, 0, 1, n)-(value)))
    plt.loglog(N, I)
    plt.xlabel("N --->")
    plt.ylabel("Error --->")
    plt.savefig("DELETE.png")
    
def bounded(f, a, b, accuracy):
    N = 100 
    #N_0, taken this value as higher N_0's were make analysis hard
    while True:
        lower = simpson(f, a, b, N)
        upper = simpson(f, a, b, 2*N)
        bound = (np.abs(lower - upper) / lower)
        if(accuracy > bound):
            break
        N *= 2
    return lower

# redundant input allows us to use compare(), plot() methods
def romberg(f, a, b, redundant):
    return sc.romberg(f, a, b)

# redundant input allows us to use compare(), plot() methods
def quad(f, a, b, redundant):
    return sc.quad(f, a, b)[0]

def compare(f_1, f_2, N_min, N_max):
    plot(f_1, N_min, N_max)
    plot(f_2, N_min, N_max)
    