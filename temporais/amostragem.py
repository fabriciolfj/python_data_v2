from pandas.tseries.offsets import MonthEnd
import pandas as pd
import numpy as np


ts = pd.Series(np.random.standard_normal(20),
               index=pd.date_range('1/1/2000', periods=20, freq="4D"))
print(ts)
print("===========")

#MonthEnd é uma classe da biblioteca pandas.tseries.offsets que representa uma deslocação para o fim do mês. Ou seja, ela ajusta uma data para o último dia do mês.
#rollforward é um método da classe MonthEnd que ajusta a data para o próximo último dia do mês, se não estiver no final do mês atual. Basicamente, ele avança a data para o fim do mês correspondente.
print(ts.groupby(MonthEnd().rollforward).mean())

print("===========")
print(ts.resample("M").count())