import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.standard_normal((10, 4)).cumsum(0),
                    columns=["A", "B", "C", "D"],
                    index=np.arange(0, 100, 10))

plt.style.use('grayscale')

df.plot()
plt.show()

