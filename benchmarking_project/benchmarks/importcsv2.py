import sqlite3
import pandas as pd
conn = sqlite3.connect('db.sqlite3')
query = "SELECT * FROM system"

df = pd.read_sql_query(query, conn)
print(df)