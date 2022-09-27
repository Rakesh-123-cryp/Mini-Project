import mysql.connector as mc
import math
sql = mc.connect(user = "" , root = "localhost" , password = "22072003Rr" , database = "MiniProject ")

cur = sql.coursor()

#---------- Search using filter ----------

#based of cuisine
filters = #input from user as  Dictionary
additional_conditions = ""
for i in filters:
    if additional_conditions != "":
        cur.execute(f"ALTER SUPPLEMENTARY AS SELECT FROM SUPPLEMENTARY WHERE {i} IN {filters.get(i)};")
    else:
        cur.execute(f"CREATE VIEW SUPPLEMENTARY AS (SELECT FROM CUSTOMERS WHERE {i} IN {filters.get(i)});")


Popularity = 1/(1+math.exp(-1*views)) * rating # Formula used to order data
