import io

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    y = np.array([35, 35, 25, 5])

    plt.pie(y)
    plt.savefig("pie.png", format="png")
    plt.show()

    # plt.savefig("pie.png")

    #Two  lines to make our compiler able to draw:
    # plt.savefig(sys.stdout.buffer)
    # sys.stdout.flush()