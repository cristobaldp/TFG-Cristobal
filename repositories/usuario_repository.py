import bcrypt

class UsuarioRepository:
    def __init__(self, db):
        self.db = db

    def insertar(self, nombre, apellidos, username, email, telefono, ciudad, fecha, password_hash):
        con = self.db.get_connection()
        cur = con.cursor()
        try:
            cur.execute("""
                INSERT INTO usuarios
                (nombre, apellidos, username, email, telefono, ciudad, fecha_nacimiento, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (nombre, apellidos, username, email, telefono, ciudad, fecha, password_hash))

            con.commit()
            return True
        except Exception as e:
            print("Error al insertar usuario:", e)
            return False
        finally:
            con.close()

    def buscar(self, usuario):
        con = self.db.get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT id, nombre, apellidos, username, email, telefono, ciudad, fecha_nacimiento, password
            FROM usuarios
            WHERE username = ? OR email = ?
        """, (usuario, usuario))

        row = cur.fetchone()
        con.close()
        return row
