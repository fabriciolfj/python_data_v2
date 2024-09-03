import numpy as np
import pandas_teste as pd


price = pd.read_pickle('yahoo_price.pkl')

#traz a variacao percentual de precos a cada valor
returns = price.pct_change()


print(returns.cov())
print(returns.corr())
