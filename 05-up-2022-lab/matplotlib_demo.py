import sys

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55, 15, 25, 5])

plt.pie(y)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
