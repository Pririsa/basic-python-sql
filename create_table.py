import sqlite3

connection = sqlite3.connect('product-db.sqlite3')
c = connection.cursor()

#Create Table
c.execute('''CREATE TABLE IF NOT EXISTS transaction_history(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quantity REAL,
                total REAL)''')

print('Success !')