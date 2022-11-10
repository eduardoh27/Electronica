import matplotlib.pyplot as plt
import numpy as np

def main():

    fig = plt.figure()
    ax = fig.add_subplot()
    #ax.set_title('Vo vs V_i')
    ax.set_xlabel('Vi',fontsize=10)
    ax.set_ylabel('Vo',fontsize=10)
    ax.set_xlim(-5,15)
    ax.set_ylim(6,12)

    plt.plot((-5,3),(8.02,8.02), c='purple')
    plt.plot((3,10.5),(10,10), c='purple')
    
    plt.savefig('tarea4sofi.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
