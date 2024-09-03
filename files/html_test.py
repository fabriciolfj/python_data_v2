import pandas_teste as pd
import lxml.html as lh

tables = pd.read_html("fdic_failed_bank_list.html")

print(len(tables))

failures = tables[0]
print(failures)

close_timestamps = pd.to_datetime(failures["Closing Date"])
print(close_timestamps.dt.year.value_counts())