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

        # Cifrar la contraseña
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        ok = self.repo.insertar(nombre, apellidos, username, email, telefono, ciudad, fecha, hashed)
        return "OK" if ok else "ERROR"

    # ============================
    # LOGIN
    # ============================
    def login(self, usuario, password):
        row = self.repo.buscar(usuario)
        if not row:
            return None

        stored_hash = row[-1]   # última columna es password hash

        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            return Usuario(*row[:-1])  # todos menos password
        return None
