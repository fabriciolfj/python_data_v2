import pandas as pd
import numpy as np

#indicado para escrita de grande informacao
frame = pd.DataFrame({"a": np.random.standard_normal(100)})

store = pd.HDFStore("mydata.h5")

store["obj1"] = frame

store["obj1_col"] = frame["a"]

print(store)

#2 modos default é fixed e table, table e mais lento no entanto suporta opecoes de consultas
store.put("obj2", frame, format="table")
result = store.select("obj2", where=["index >= 10 and index <=15"])
print(result)
store.close()


frame.to_hdf("mydata.h5", key="obj3", format="table")
pd.read_hdf("mydata.h5", key="obj3", where=["index < 5"])