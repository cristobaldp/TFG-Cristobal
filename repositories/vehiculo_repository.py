class VehiculoRepository:
    def __init__(self, db):
        self.db = db

    def insertar(self, user_id, tipo, marca, modelo, matricula, anio, combustible, consumo):
        con = self.db.get_connection()
        cur = con.cursor()
        try:
            cur.execute("""
                INSERT INTO vehiculos 
                (user_id, tipo, marca, modelo, matricula, anio, combustible, consumo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (user_id, tipo, marca, modelo, matricula, anio, combustible, consumo))
            con.commit()
            return True
        except Exception as e:
            print("ERROR al insertar vehículo:", e)
            return False
        finally:
            con.close()

    def obtener_por_usuario(self, user_id):
        con = self.db.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM vehiculos WHERE user_id = ?", (user_id,))
        datos = cur.fetchall()
        con.close()
        return datos

    def eliminar(self, id_vehiculo):
        con = self.db.get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM vehiculos WHERE id = ?", (id_vehiculo,))
        con.commit()
        con.close()
