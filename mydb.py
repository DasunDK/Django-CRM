import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#prepare cursor object
cursorObject = dataBase.cursor()

# create a databse
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")