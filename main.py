import traceback

from DataExtraction.get_rr_list import get_rr_list
from HRV.metrics import BPM, IBI, SDNN, SDSD, sympatho_vagal_balance
import pandas as pd
import numpy as np


def main():
    try:
        data = pd.read_csv('cardiac_signal.csv')
        x = get_rr_list(data)
        BPM(x)
        IBI(x)
        SDNN(x)
        print("SDSD: ", np.std(SDSD(x)))
        print("RMSD: ", np.sqrt(np.mean(SDSD(x))))
        print("Sympatho-vagal balance: ", np.sqrt(np.mean(sympatho_vagal_balance(x))))

    except Exception as error:
        print(traceback.format_exc())


if __name__ == "__main__":
    main()