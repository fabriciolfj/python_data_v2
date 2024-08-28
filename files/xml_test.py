import pandas as pd


path = "../datasets/mta_perf/Performance_MNR.xml"

p = pd.read_xml(path)

print(p.head())