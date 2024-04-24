import config

def create_table():
    conn = config.connect_postgres()
    cursor = conn.cursor()
    cursor.execute( 
        '''CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY, \
        name varchar(100), \
        created timestamp DEFAULT current_timestamp);'''
    )
    conn.commit()
    cursor.close()
    conn.close() 


def insert_data(names):
    conn = config.connect_postgres()
    cursor = conn.cursor()
    for name in names:
        cursor.execute('''INSERT INTO users (name) VALUES (%s)''', (name,))
    conn.commit()
    cursor.close()
    conn.close() 


def fetch_data():
    conn = config.connect_postgres()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data