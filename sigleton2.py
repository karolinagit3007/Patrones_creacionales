
import sqlite3

class DatabaseConnection:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super(DatabaseConnection, cls).__new__(cls)
            return cls._instance
        
        def __init__(self, db_name):
            if not hasattr(self, '_connection'):
                self._connection = sqlite3.connect(db_name)
                self._cursor = self._connection.cursor()
        
        def query(self, sql, params=[]):
            self._cursor.execute(sql, params)
            self._connection.commit()
            return self._cursor
        
        def fetch(self):
            return self._cursor.fetchall()
            
        def close(self):
            self._connection.close()
            DatabaseConnection._instance = None

db1 = DatabaseConnection('database.db')
db2 = DatabaseConnection('database.db')

db1.query('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT) ')
db1.query('INSERT INTO users (name) VALUES (?)', ('John Doe',))
db1.query('INSERT INTO users (name) VALUES (?)', ('Jane Doe',))

db2.query(' INSERT INTO users (name) VALUES (?)', ('Juan Perez',)) 
db2.query('SELECT * FROM users')
print(db2.fetch())

db1.close()