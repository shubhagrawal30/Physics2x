import numpy as np
from matplotlib import pyplot as plt

def explicit(x_0, v_0, h, N):
    x = np.zeros(N)
    v = np.zeros(N)
    t = np.arange(0, h*N, h)
    x[0] = x_0
    v[0] = v_0
    for i in range(N-1):
        x[i+1] = x[i] + h*v[i]
        v[i+1] = v[i] - h*x[i]
    return (x, v, t)
    
def plot(x, v, t):
    plt.figure(0)
    plt.plot(t, x)
    plt.xlabel("t --->")
    plt.ylabel("Error in x --->")
    plt.savefig("delete.png")
    
    plt.figure(1)
    plt.plot(t, v)
    plt.xlabel("t --->")
    plt.ylabel("Error in v --->")
    plt.savefig("delete.png")
    
def plotlinear(X, Y):
    plt.figure(2)
    plt.plot(X, Y)
    plt.ylabel("energy --->")
    plt.xlabel("time --->")
    plt.savefig("delete.png")
    
def plotlog(X, Y):
    plt.figure(2)
    plt.loglog(X, Y, basex=2, basey=2)
    plt.xlabel("Maximum error (x-based)--->")
    plt.ylabel("h --->")
    plt.savefig("delete.png")
    
def error(f, h, N):
    x, v, t = f(1, 0, h, N)
    x_a = np.cos(t)
    v_a = -1 * np.sin(t)
    ex = x_a - x
    ev = v_a - v
    plot(ex, ev, t)
    return (ex, ev)

def truncation(f, h, N):
    hv = np.zeros(5)
    te = np.zeros(5)
    for i in np.arange(5):
        ex, ev = error(f, h, int(25/h))
        te[i] = np.max(ex)
        hv[i] = h
        h/=2
    plotlinear(hv, te)
    
def energy(f, h, N):
    x, v, t = f(1, 0, h, N)
    en = x * x + v * v
    plotlinear(t, en)

def implicit(x_0, v_0, h, N):
    x = np.zeros(N)
    v = np.zeros(N)
    t = np.arange(0, h*N, h)
    x[0] = x_0
    v[0] = v_0
    for i in range(N-1):
        x[i+1] = (x[i] + h*v[i]) / (1 + h**2)
        v[i+1] = (v[i] - h*x[i]) / (1 + h**2)
    return (x, v, t)

def phase(f, h, N):
    x, v, t = f(1, 0, h, N)
    plotlinear(x, v)
    
def euler(x_0, v_0, h, N):
    x = np.zeros(N)
    v = np.zeros(N)
    t = np.arange(0, h*N, h)
    x[0] = x_0
    v[0] = v_0
    for i in range(N-1):
        x[i+1] = (x[i] + h*v[i])
        v[i+1] = (v[i] - h*x[i+1])
    return (x, v, t)

def compare(h, N):
    x, v, t = explicit(1, 0, h, N)
    xA, vA, tA = implicit(1, 0, h, N)
    plt.figure(0)
    plt.plot(t, x, label="Explicit")
    plt.plot(tA, xA, label="Implicit")
    plt.xlabel("t --->")
    plt.ylabel("x --->")
    plt.legend(loc='lower left')
    plt.savefig("cx.png")
    
    plt.figure(1)
    plt.plot(t, v, label="Explicit")
    plt.plot(tA, vA, label="Implicit")
    plt.xlabel("t --->")
    plt.ylabel("v --->")
    plt.legend(loc='upper left')
    plt.savefig("cv.png")
    
def compare_stuff(f, h, N):
    f(explicit, h, N)
    f(implicit, h, N)
    plt.legend(["Explicit", "Implicit"])
    plt.savefig("delete.png")