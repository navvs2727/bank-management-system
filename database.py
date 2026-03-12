import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Waheguruji@27.",
    database="bankdb"
)

cursor = db.cursor()