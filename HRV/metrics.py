import numpy as np
import math


def BPM(distancebtwpeaks):
    bpm = 60 / np.mean(distancebtwpeaks)
    y = print("BPM moyen:", bpm)

    return y


def IBI(distancebtwpeaks):
    for i in distancebtwpeaks:
        IBI = 60 / (i + 1)
        IBI += IBI

    IBImoy = IBI / np.mean(distancebtwpeaks)
    x = print("IBI moyen:", IBImoy)
    return x


def SDNN(distancebtwpeaks):
    RR_diff = []
    cnt = 1
    while (cnt < len(distancebtwpeaks) - 1):
        RR_diff.append(abs(distancebtwpeaks[cnt] - distancebtwpeaks[cnt + 1]))
        cnt += 1
    # print(RR_diff)
    sdnn = np.std(distancebtwpeaks)
    print("SDNN:", sdnn)
    return RR_diff


def SDSD(distancebtwpeaks):
    RR_sqdiff = []
    cnt = 1
    while (cnt < len(distancebtwpeaks) - 1):
        RR_sqdiff.append(math.pow(distancebtwpeaks[cnt] - distancebtwpeaks[cnt + 1], 2))
        cnt += 1
    #print(RR_sqdiff)
    return RR_sqdiff


def sympatho_vagal_balance(distancebtwpeaks):
    f1 = 80
    n1 = len(distancebtwpeaks)+1
    frq1 = np.fft.fftfreq(n1, d=(1. / f1))
    frq1 = frq1[range(n1 // 2)]
    # print(frq1)
    f2 = 200
    n2 = len(distancebtwpeaks)
    frq2 = np.fft.fftfreq(n2, d=(1. / f2))
    frq2 = frq2[range(n2 // 2)]
    # print(frq2)
    svb = frq2/frq1[1:]
    # print(svb)
    return svb
