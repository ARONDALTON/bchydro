from matplotlib import pyplot as plt
import bchydro
#import numpy as np

def differentMags():
    M = [5, 6, 7, 8]
    Rrup = [10, 10, 10, 10]
    Rhyp = [10, 10, 10, 10]
    eventType = [0, 0, 0, 0]
    Z = [5, 5, 5, 5]
    Faba = [1, 1, 1, 1]
    Vs30 = [760, 760, 760, 760]
    periods = [0.01, 0.02, 0.05, 0.075, 0.1, 0.15, 0.2, 0.250, 0.3, 0.4, 0.5, 0.6, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.5, 10.0]
    spectra = bchydro.spectra(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods)
    plt.loglog(periods, spectra[0] , 'r', periods, spectra[1] , '--r', periods, spectra[2] , 'g', periods, spectra[3] , '--g')
    plt.ylabel('Sa')
    plt.show()

def plotCoefs():
    periods = [0.01, 0.02, 0.05, 0.075, 0.1, 0.15, 0.2, 0.250, 0.3, 0.4, 0.5, 0.6, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.5, 10.0]

    plt.semilogx(periods, bchydro.model.VLIN)
    plt.ylabel('YLIN')
    plt.show()

    plt.semilogx(periods, bchydro.model.B)
    plt.ylabel('B')
    plt.show()

    plt.semilogx(periods, bchydro.model.T1)
    plt.ylabel('T1')
    plt.show()

    plt.semilogx(periods, bchydro.model.T2)
    plt.ylabel('T2')
    plt.show()

    plt.semilogx(periods, bchydro.model.T6)
    plt.ylabel('T6')
    plt.show()

    plt.semilogx(periods, bchydro.model.T7)
    plt.ylabel('T7')
    plt.show()


    plt.semilogx(periods, bchydro.model.T8)
    plt.ylabel('T8')
    plt.show()

    plt.semilogx(periods, bchydro.model.T10)
    plt.ylabel('T10')
    plt.show()

    plt.semilogx(periods, bchydro.model.T11)
    plt.ylabel('T11')
    plt.show()

    plt.semilogx(periods, bchydro.model.T12)
    plt.ylabel('T12')
    plt.show()

    plt.semilogx(periods, bchydro.model.T13)
    plt.ylabel('T13')
    plt.show()

    plt.semilogx(periods, bchydro.model.T14)
    plt.ylabel('T14')
    plt.show()

    plt.semilogx(periods, bchydro.model.T15)
    plt.ylabel('T15')
    plt.show()

    plt.semilogx(periods, bchydro.model.T16)
    plt.ylabel('T16')
    plt.show()

if __name__ == '__main__':
    differentMags()
    plotCoefs()
