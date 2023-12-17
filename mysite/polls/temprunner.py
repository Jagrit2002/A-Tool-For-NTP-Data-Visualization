import pandas as pd
import sqlite3
a= str(object = '11:28:30')
b = str(object='13:35:37')
c = str(object = '2023-06-20')
s = str(object = '5')
sql_connect = sqlite3.connect(r'C:\\Users\\hp\\OneDrive\\Desktop\\django\\mysite\\lite.sqlite3')
cursor = sql_connect.cursor()
query = "SELECT * FROM t WHERE date > (SELECT date('now', ? || 'day'))"
# query = "SELECT * FROM t WHERE pc_time BETWEEN :x AND :y AND date = :z"
# query.bind_param(1,a)
# z = query.execute
# query = "SELECT * FROM t WHERE date > to_date(:x , 'YYYY-MON-DD')"
# query = "SELECT * FROM t WHERE date < (date('now') -5)"
# query = "SELECT * FROM t WHERE date >= (SELECT DATEADD(date, -5, GETDATE()))"
# query = "SELECT * FROM t WHERE date > date('now') -:x ,'day' "
df =pd.read_sql_query(query,sql_connect , params=(s,) )
cursor.execute(query , (s,))
# # print(df)
print(cursor.fetchall())
sql_connect.close()
print(df)