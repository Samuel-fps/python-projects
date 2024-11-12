import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE store (item TEEXT, quantity INTEGER, PRICE real)")

    conn.commit()
    conn.close()

def insert_item(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

    conn.commit()
    conn.close()

def view_items():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    rows = cur.execute("SELECT * FROM store").fetchall()

    conn.commit()
    conn.close()

    return rows

insert_item("Mesa", 5, 80)
print(view_items())
