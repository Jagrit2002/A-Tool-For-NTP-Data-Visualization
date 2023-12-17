import pandas as pd
import sqlite3
a= 5
sql_connect = sqlite3.connect(r'C:\\Users\\hp\\OneDrive\\Desktop\\django\\mysite\\lite.sqlite3')
cursor = sql_connect.cursor()
query = "SELECT * FROM t WHERE date <= (SELECT date('now', :x 'day'))"
# query.bind_param(1,a)
# z = query.execute
# query = "SELECT * FROM t WHERE date > to_date(:x , 'YYYY-MON-DD')"
# query = "SELECT * FROM t WHERE date < (date('now') -5)"
# query = "SELECT * FROM t WHERE date >= (SELECT DATEADD(date, -5, GETDATE()))"
# query = "SELECT * FROM t WHERE date > date('now') -:x ,'day' "
df =pd.read_sql_query(query,sql_connect , params={'x':a})
# z=cursor.execute(query , (a,))
# # print(df)
# print(cursor.fetchall())
sql_connect.close()
print(df)