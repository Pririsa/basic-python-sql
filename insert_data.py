import sys
import sqlite3
from os.path import dirname
root_dir = dirname(__file__)
sys.path.append(root_dir)

def add_transaction_history(data):
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quantity = data['quantity']
    total = data['total']

    connection = sqlite3.connect('product-db.sqlite3')
    c = connection.cursor()

    with connection:
        command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
        c.execute(command, (ID, tid, stamp, product, price, quantity, total))
        connection.commit()

    print('inserted successfully!')

transaction_data = {
    'tid': '1234567',
    'stamp': '2021-12-12 11:47:00',
    'product': 'durian',
    'price': 100,
    'quantity': 50,
    'total': 5000
}
add_transaction_history(transaction_data)
