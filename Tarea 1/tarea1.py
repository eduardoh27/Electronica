import matplotlib.pyplot as plt
import numpy as np

def main():
    
    plt.style.use(['science','no-latex'])
    
    A = 1
    
    voltaje = lambda t : 5.028*np.exp(-(50/9) * 1e6 * t) + 16.971
    
    tiempo = np.linspace(0, 1e-6, 100)
    
    print(voltaje(1e-5))
     
    lista_y = voltaje(tiempo)
       
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('Tiempo',fontsize=10)
    ax.set_ylabel('$Voltaje$',fontsize=10)
    plt.plot(tiempo, lista_y)
    
    plt.savefig('tarea1electronica.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    