import sqlite3

DATABASE_NAME = "birthdayverse.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        phone TEXT,

        password TEXT NOT NULL,

        birthday TEXT,

        gender TEXT,

        profile_image TEXT,

        role TEXT DEFAULT 'user',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wishes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sender_id INTEGER,

        receiver_id INTEGER,

        message TEXT,

        visible_on TEXT,

        anonymous INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        quote TEXT,

        author TEXT,

        language TEXT,

        category TEXT

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        title TEXT,

        body TEXT,

        is_read INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    connection.commit()

    connection.close()


def execute_query(query, values=()):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, values)

    connection.commit()

    connection.close()


def fetch_one(query, values=()):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, values)

    row = cursor.fetchone()

    connection.close()

    return row


def fetch_all(query, values=()):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, values)

    rows = cursor.fetchall()

    connection.close()

    return rows