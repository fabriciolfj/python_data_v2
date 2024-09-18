import matplotlib.pyplot as plt
import numpy as np

plt.subplots(2, 2, sharex=True, sharey=True)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

ax3.plot(np.random.standard_normal(50).cumsum(), color="green", linestyle="--", marker="o")
ax1.hist(np.random.standard_normal(100), bins=20, color="black", alpha=0.5)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30))

fig.subplots_adjust(wspace=0.2, hspace=0.2)

plt.show()