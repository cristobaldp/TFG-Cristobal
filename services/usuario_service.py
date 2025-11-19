from models.Usuario import Usuario
import bcrypt
import re

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo

    # ============================
    # VALIDACIONES
    # ============================
    def validar_email(self, email):
        patrones = [
            r"^[a-zA-Z0-9._%+-]+@gmail\.com$",
            r"^[a-zA-Z0-9._%+-]+@hotmail\.com$",
            r"^[a-zA-Z0-9._%+-]+@outlook\.com$"
        ]
        return any(re.match(p, email) for p in patrones)

    def validar_telefono(self, tel):
        return tel.isdigit() and 9 <= len(tel) <= 12

    # ============================
    # REGISTRO
    # ============================
    def registrar(self, nombre, apellidos, username, email, telefono, ciudad, fecha, password):
        if not self.validar_email(email):
            return "EMAIL_INVALIDO"

        if not self.validar_telefono(telefono):
            return "TELEFONO_INVALIDO"

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        ok = self.repo.insertar(nombre, apellidos, username, email, telefono, ciudad, fecha, hashed)
        return "OK" if ok else "ERROR"

    # ============================
    # LOGIN
    # ============================
    def login(self, usuario, password):
      row = self.repo.buscar(usuario)
      if not row:
        return None  # usuario no encontrado

      stored_hash = row[-1]   # hash en la última columna

      if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        # Crear objeto Usuario EXACTO en el orden correcto
        return Usuario(
            row[0],  # id
            row[1],  # nombre
            row[2],  # apellidos
            row[3],  # username
            row[4],  # email
            row[5],  # telefono
            row[6],  # ciudad
            row[7]   # fecha_nacimiento
        )
      return None
