import matplotlib.pyplot as plt
import numpy as np

def main():

    plt.style.use(['science','no-latex'])
    
    def vo(vi):

        if vi<3:
            return 8.02 
        elif vi>3 and vi <= 10.5:
            return 10
        else:
            return 0

    #lista_vi = np.linspace(-5, 12, int(1e6))
    #lista_vo = [vo(vi) for vi in lista_vi]
    #plt.plot(lista_vi, lista_vo)


    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('$V_o$ vs $V_i$')
    ax.set_xlabel('$V_i$ (V)',fontsize=10)
    ax.set_ylabel('$V_o$ (V)',fontsize=10)
    ax.set_xlim(-5,12)
    ax.set_ylim(5,15)

    plt.plot((-5,3),(8.02,8.02), c='b')
    plt.plot((3,10.5),(10,10), c='b')
    
    plt.savefig('tarea4edu.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
