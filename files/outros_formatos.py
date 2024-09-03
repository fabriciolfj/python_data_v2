import pandas_teste as pd
import csv

f = open("ex7.csv")

reader = csv.reader(f)

for line in reader:
    print(line)

with open('ex7.csv') as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]

data_dict = {h: v for h, v in zip(header, zip(*values))}

print(data_dict)

class my_dialect(csv.Dialect):
    lineterminator = "\n"
    delimiter = ";"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(("one", "two", "three"))
    writer.writerow(("1", "2", "3"))
    writer.writerow(("3", "4", "5"))


