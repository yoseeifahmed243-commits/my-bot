import sqlite3

DB_NAME = "bot.db"


def connect():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


conn = connect()
cursor = conn.cursor()


# إنشاء الجداول
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service TEXT,
    link TEXT,
    quantity INTEGER,
    price REAL,
    status TEXT DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


# إضافة مستخدم
def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    conn.commit()


# الرصيد
def get_balance(user_id):
    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else 0


# تعديل الرصيد
def update_balance(user_id, amount):
    cursor.execute(
        "UPDATE users SET balance=? WHERE user_id=?",
        (amount, user_id)
    )
    conn.commit()


# إنشاء طلب
def create_order(user_id, service, link, quantity, price):
    cursor.execute("""
        INSERT INTO orders
        (user_id, service, link, quantity, price)
        VALUES(?,?,?,?,?)
    """, (user_id, service, link, quantity, price))
    conn.commit()


# جميع الطلبات
def get_orders():
    cursor.execute("SELECT * FROM orders ORDER BY id DESC")
    return cursor.fetchall()
