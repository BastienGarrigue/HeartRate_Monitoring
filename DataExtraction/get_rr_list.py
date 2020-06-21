from DataExtraction.detect_peaks import detect_peaks


def get_rr_list(data):
    # implémenter fonction de détection de pics
    X = data['amplitude']
    peaks = detect_peaks(X, mpd=100)
    time_peak = []
    for peaks in peaks:
        time_peak.append(data["time"][peaks])

    rr_list = []

    # creation d'une liste avec l'intervalle entre les battements de coeurs
    for i in range(0, len(time_peak) - 1):
        rr_list.append(abs(time_peak[i] - time_peak[i + 1]))

    return rr_list