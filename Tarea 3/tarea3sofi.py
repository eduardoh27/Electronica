import matplotlib.pyplot as plt
import numpy as np

def main():

    #plt.style.use(['science','no-latex'])
    
    """
    def voltaje(t): 
        print(t)
        if t < 0:
            return 18
        else:
            return 5.028*np.exp(-(50/9) * 1e6 * t) + 16.971
    """
    
    l, c = 100e-3, 100e-6
    
    vo = lambda w, vi : np.abs( vi * (1- (w**2)*l*c) )
    
    omegas = np.linspace(0, 1e3, 100000)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('Magnitud de V_o para diferentes V_i')
    ax.set_xlabel('$w$ (rad/s)',fontsize=10)
    ax.set_ylabel('$v_o(w)$ (V)',fontsize=10)
    
    lista_colores = ['pink', 'purple', 'black'] 
    lista_vi = [2, 4, 8]
    
    for i in range(3):
        plt.plot(omegas, vo(omegas, lista_vi[i]), color=lista_colores[i])
    
    plt.savefig('tarea3sofi.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    