import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv("../files/tips.csv")
tips["tip_pct"] = tips["tip"] / (tips["total_bill"] - tips["tip"])
print(tips.head())

sns.barplot(x="tip_pct", y="day", data=tips, orient="h")
plt.show()
