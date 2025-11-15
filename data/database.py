import sqlite3

DB_NAME = "usuarios.db"

class Database:
    def __init__(self):
        self.create_tables()

    def get_connection(self):
        return sqlite3.connect(DB_NAME)

    def create_tables(self):
        con = self.get_connection()
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellidos TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                telefono TEXT NOT NULL,
                ciudad TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)

        # Tabla de vehículos
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vehiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                matricula TEXT NOT NULL UNIQUE,
                anio INTEGER NOT NULL,
                combustible TEXT NOT NULL,
                consumo REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES usuarios(id)
            )
        """)

        con.commit()
        con.close()
