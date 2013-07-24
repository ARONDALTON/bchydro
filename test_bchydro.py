import bchydro
from nose.tools import raises
import itertools

@raises(Exception)
def test_inputLengthCheck():
    M = [5.5 , 6, 5]
    Rrup = [4 , 5, 6]
    Rhyp = [5, 6, 7]
    eventType = [0 , 1]
    Z = [1 , 2, 3]
    Faba = [0 , 0 , 1]
    Vs30 = [1 , 2]
    periods = [1 , 2, 3 , 4]
    bchydro.spectra(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods)

@raises(Exception)
def test_periodCheck():
    M = [5.5 , 6, 5]
    Rrup = [4 , 5, 6]
    Rhyp = [5, 6, 7]
    eventType = [0 , 1, 1]
    Z = [1 , 2, 3]
    Faba = [0 , 0 , 1]
    Vs30 = [1 , 2, 1]
    periods = []
    bchydro.spectra(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods)

def check_spectraLength(M , Rrup, Rhyp, eventType, Z, Faba, Vs30, periods):
    spectra = bchydro.spectra(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods)
    print spectra
    assert len(spectra) == len(M)
    assert len(spectra[0]) == len(periods)

def test_spectraLength():
    M = [[5.5 , 6, 5] , [5, 6] , [6]]
    Rrup = [[4 , 5, 6] , [10, 5] , [1]]
    Rhyp = [[5, 6, 7] , [10, 5] , [2]]
    eventType = [[0, 1, 1], [0, 0] , [1]]
    Z = [[1, 2, 3] , [1.1, 2.2] , [2.4]]
    Faba = [[0 , 0 , 1] , [0 , 0] , [1]]
    Vs30 = [[700 , 500, 200] , [800 , 400] , [760]]
    periods = [[1 , 2], [0.1, 0.2, 0.3, 0.4, 1, 2] , [1.0, 2.0, 3.0, 4.1]]

    for m, rrup, rhyp, evtype, z, faba, vs30, per in itertools.izip(M, Rrup, Rhyp, eventType, Z, Faba, Vs30, periods):
        yield 'check_spectraLength', m, rrup, rhyp, evtype, z, faba, vs30, per

def test_coefLengths():
    assert len(bchydro.model.VLIN) == 23
    assert len(bchydro.model.B) == 23
    assert len(bchydro.model.T1) == 23
    assert len(bchydro.model.T2) == 23
    assert len(bchydro.model.T6) == 23
    assert len(bchydro.model.T7) == 23
    assert len(bchydro.model.T8) == 23
    assert len(bchydro.model.T10) == 23
    assert len(bchydro.model.T11) == 23
    assert len(bchydro.model.T12) == 23
    assert len(bchydro.model.T13) == 23
    assert len(bchydro.model.T14) == 23
    assert len(bchydro.model.T15) == 23
    assert len(bchydro.model.T16) == 23
