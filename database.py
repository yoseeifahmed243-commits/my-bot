import sqlite3

db = sqlite3.connect("bot.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0,
    orders INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service TEXT,
    country TEXT,
    price REAL,
    status TEXT
)
""")

db.commit()


def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    db.commit()


def get_balance(user_id):
    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )
    data = cursor.fetchone()

    if data:
        return data[0]

    return 0


def add_balance(user_id, amount):
    cursor.execute(
        "UPDATE users SET balance=balance+? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def remove_balance(user_id, amount):
    cursor.execute(
        "UPDATE users SET balance=balance-? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()


def add_order(user_id, service, country, price):
    cursor.execute(
        "INSERT INTO orders(user_id,service,country,price,status) VALUES(?,?,?,?,?)",
        (user_id, service, country, price, "Pending")
    )

    cursor.execute(
        "UPDATE users SET orders=orders+1 WHERE user_id=?",
        (user_id,)
    )

    db.commit()
