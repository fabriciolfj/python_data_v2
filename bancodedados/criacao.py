import sqlite3
import pandas as pd

query = """
    CREATE TABLE TEST (
        a varchar(20),
        b varchar(20),
        c REAL,
        d INTEGER
    );
"""

con = sqlite3.connect("mydata.sqlite")
#con.execute(query)
con.commit()

data = [
    ("Atlanta", "Georgia", 1.25, 6),
    ("Tallahasse", "Florida", 2.6, 3),
    ("Sacramento", "California", 1.7, 5),
]

smt = "INSERT INTO TEST (a, b, c, d) VALUES (?, ?, ?, ?)"
con.executemany(smt, data)
con.commit()

cursor = con.execute("SELECT * FROM TEST")

rows = cursor.fetchall()

print(rows)

result = pd.read_sql("SELECT * FROM TEST", con)

print(result)
con.close()