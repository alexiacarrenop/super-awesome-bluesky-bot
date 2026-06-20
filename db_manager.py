import sqlite3
from random import randint

con = sqlite3.connect("database.db")
cur = con.cursor()

def create_table():   
    cur.execute("CREATE TABLE posts(" \
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
    "post_text VARCHAR(255) NOT NULL, " \
    "scheduled_date TEXT," \
    "has_been_posted BOOLEAN DEFAULT 0)")
    con.commit()

def insert_data():
    cur.execute("""
    INSERT INTO posts (post_text, scheduled_date)
                VALUES
    ('and suddenly hades was only a man, with a taste of nectar upon his lips', '2026-06-19'),
    ('to know how it ends and still begin to sing it again, as if it might turn out this time. i learnt that from a friend of mine', '2026-06-21'),
    ('it was like holding the world when you held her, like yours were the arms that the whole world was in. and there were no words for the way that you felt, so you opened your mouth and you started to sing', '2026-06-22')
    """)
    con.commit()

def get_random_quote():
    num = randint(1,3)
    
    cur.execute("SELECT post_text FROM posts WHERE id = (?)", (num,))    
    result = cur.fetchone()

    if result:
        return result[0]
    return None

# create_table()
# insert_data()
