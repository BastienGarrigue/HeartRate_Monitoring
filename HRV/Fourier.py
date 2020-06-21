import numpy as np


def fourier(data):
    f = 200
    n = len(data["amplitude"])
    frq = np.fft.fftfreq(n, d=(1. / f))
    frq = frq[range(n // 2)]

    return frq
