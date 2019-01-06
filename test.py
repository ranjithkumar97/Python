import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sandy",

    database="sandy"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user432")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  print("hello")