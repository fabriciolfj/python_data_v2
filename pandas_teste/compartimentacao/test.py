import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

age_categories = pd.cut(ages, bins)

print(age_categories.value_counts())

print("===============")
#colocando labels
group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]

age_categories = pd.cut(ages, bins, labels=group_names)
print(age_categories.value_counts())