import matplotlib.pyplot as plt
import numpy as np

def main():

    plt.style.use(['science','no-latex'])

    l, c = 100e-3, 100e-6    
    vo = lambda w, vi : np.abs( vi * (1- (w**2)*l*c) )
    
    omegas = np.linspace(0, 1.2e3, 100000)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('$|v_o(\omega)|$ para varios $V_i$')
    ax.set_xlabel('$\omega$ (rad/s)',fontsize=10)
    ax.set_ylabel('$|v_o(\omega)|$ (V)',fontsize=10)
    
    lista_colores = ['red', 'blue', 'green', 'purple', 'black'] 
    lista_vi = [0, 2, 4, 8]
    
    for i in range(4):
        plt.plot(omegas, vo(omegas, lista_vi[i]), color=lista_colores[i], label = f'$V_i = {lista_vi[i]} V$')
        
    ax.legend(loc ="upper left")
    
    plt.savefig('tarea3edu.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    