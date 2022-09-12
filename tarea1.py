import matplotlib.pyplot as plt
import numpy as np

def main():

    #plt.style.use(['science','no-latex'])
    
    def voltaje(t): 
        print(t)
        if t < 0:
            return 18
        else:
            return 5.028*np.exp(-(50/9) * 1e6 * t) + 16.971

    
    tiempo = np.linspace(-1e-6, 1e-6, 1000)
    lista_y = [voltaje(i) for i in tiempo]
       
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('$t$ (s)',fontsize=10)
    ax.set_ylabel('$v(t)$ (V)',fontsize=10)
    plt.plot(tiempo, lista_y)
    
    plt.savefig('tarea1electronica.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    