''' Implementation of the BC Hydro model'''
import numpy as np

def spectra(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods):
    nRow = len(M)
    nCol = len(periods)

    M = np.array([M] * nCol).transpose()
    Rrup = np.array([Rrup] * nCol).transpose()
    Rhyp = np.array([Rhyp] * nCol).transpose()
    eventType = np.array([eventType] * nCol).transpose()
    Z = np.array([Z] * nCol).transpose()
    Faba = np.array([Faba] * nCol).transpose()
    Vs30 = np.array([Vs30] * nCol).transpose()
    periods = np.array([periods] * nRow)

    return M
