import psycopg2

def connect_postgres():
    return psycopg2.connect(database="pgdb", 
                            user="pguser", 
                            password="pgpass", 
                            host="localhost", port="5432") 
