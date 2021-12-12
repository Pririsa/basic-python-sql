import sys
import sqlite3
from os.path import dirname
root_dir = dirname(__file__)
sys.path.append(root_dir)

def search_transaction_history():

    connection = sqlite3.connect('product-db.sqlite3')
    c = connection.cursor()

    with connection:
        command = 'SELECT * FROM transaction_history'
        c.execute(command)
        data = c.fetchall()
        print('data :', data)

    print('search successfully!')

search_transaction_history()