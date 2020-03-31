import numpy as np
import matplotlib.pyplot as plt

def crear_plot_radial( theta=[], medicion=[], rmax=10, path='./' ): 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="polar")
    ax.scatter(theta, medicion)
    ax.set_rmax( rmax )
    plt.savefig( path )