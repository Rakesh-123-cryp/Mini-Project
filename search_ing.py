import mysql.connector as mc
import math
sql = mc.connect(user = "" , root = "localhost" , password = "22072003Rr" , database = "MiniProject ")

cur = sql.coursor()

cur.execute("SELECT * FROM Table_Name WHERE Ingredients LIKE """)
