import matplotlib.pyplot as plt
import numpy as np

def main():
    
    plt.style.use(['science','no-latex'])
    
    a = lambda w : (2e6)*(1 - (w**2)*5e-11)
    b = lambda w : (2e6)-((w**2)*5e-11)
    
    # sumando
    amplitud = lambda w : (np.sqrt( ( ( 750*(w**2)*((b(w)**2) + 225*(w**2)) ) + ( 6e8*w*((a(w)**2) + 225*(w**2)) ) )**2 + ((50*a(w)*w*((b(w)**2)+225*(w**2))) + (4e7*b(w)*((a(w)**2) + 225*(w**2))))**2  )) / ( ((a(w)**2) + 225*(w**2)) * ((b(w)**2) + 225*(w**2)) ) 
    fase = lambda w: np.arctan( ( (50*a(w)*w*((b(w)**2)+225*(w**2))) + (4e7*b(w)*((a(w)**2) + 225*(w**2))) ) / ( ( 750*(w**2)*((b(w)**2) + 225*(w**2)) ) + ( 6e8*w*((a(w)**2) + 225*(w**2)) ) ) )
    
    """
    # restando
    #amplitud = lambda w : (np.sqrt( ( ( 750*(w**2)*((b(w)**2) + 225*(w**2)) ) - ( 6e8*w*((a(w)**2) + 225*(w**2)) ) )**2 + ((50*a(w)*w*((b(w)**2)+225*(w**2))) - (4e7*b(w)*((a(w)**2) + 225*(w**2))))**2  ))   /    ( ((a(w)**2) + 225*(w**2)) * ((b(w)**2) + 225*(w**2)) )
    #fase = lambda w: np.arctan( ( (50*a(w)*w*((b(w)**2)+225*(w**2))) - (4e7*b(w)*((a(w)**2) + 225*(w**2))) ) / ( ( 750*(w**2)*((b(w)**2) + 225*(w**2)) ) - ( 6e8*w*((a(w)**2) + 225*(w**2)) ) ) )
    """
    
    omegas = np.linspace(0.01, 1e6, 100000)
     
    #print(amplitud(20000)) # 20.28 V sumando     19.27 V restando  3183 Hz
    
    amplitudes = amplitud(omegas)
    fases = fase(omegas)
    
    # plot de amplitudes
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('$\omega \,(rad/s)$',fontsize=10)
    ax.set_ylabel('Amplitud (V)',fontsize=10)
    
    plt.plot(omegas, amplitudes)
    plt.savefig('tarea2_amplitudes.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    
    # plot de fases
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('$\omega \,(rad/s)$',fontsize=10)
    ax.set_ylabel('Fase (rad)',fontsize=10)
    
    plt.plot(omegas, fases)
    plt.savefig('tarea2_fases.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    
    """
    # plot de V vs t
    fase = 0
    w = 20000
    amplitud = 20.28
    tiempos = np.linspace(0, 1e-2, 1000)
    voltajes = lambda t : amplitud * np.sin(w*t + fase)
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('$t$',fontsize=10)
    ax.set_ylabel('$V$',fontsize=10)
    
    plt.plot(tiempos, voltajes(tiempos))
    #plt.savefig('tarea2_fases.png', dpi=300, bbox_inches='tight')
    plt.show()
    """
 
if __name__ == "__main__":

    main()
    