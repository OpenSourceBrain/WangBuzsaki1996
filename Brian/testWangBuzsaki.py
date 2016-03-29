from brian import *
import matplotlib.pyplot as plt
import sys
from WangBuzsaki import main


if __name__ == '__main__':
    
    dt = 0.001
    M = main(dt)

    # save trace to file
    if not '-nogui' in sys.argv:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(M.times, M[0]/mV)
        ax.plot([0, 0.1], [-52, -52], 'k--')
        ax.set_xlabel("Time (s)")
        ax.set_xlim([0, 0.1])
        ax.set_ylabel("Membrane Potential (mV)")
        ax.set_title('Wang Buzsaki PV cell model with 2uA input')
        plt.show()

    # save trace to file
    save = True
    if save:
        filename = 'wangbuzsaki.dat'
        outfile = open(filename, 'w')
        t = M.times.tolist()
        v = M[0].tolist()
        print("Saving results to: %s" %filename)
        for i in range(len(t)):
            line = '%s\t%s\n'%(t[i], v[i])
            outfile.write(line)
        outfile.close()
