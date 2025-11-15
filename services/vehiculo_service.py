import json
import re
class VehiculoService:
    def __init__(self, path_json="data/marcas_modelos.json"):
        self.path = path_json
        self.data = self._cargar_json()

    def _cargar_json(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def obtener_tipos(self):
        return list(self.data.keys())

    def obtener_marcas(self, tipo):
        return list(self.data.get(tipo, {}).keys())

    def obtener_modelos(self, tipo, marca):
        return self.data.get(tipo, {}).get(marca, [])

    def validar_vehiculo(self, matricula, anio, consumo):
    
    # =============================
    # VALIDAR MATRÍCULA ESPAÑOLA
    # =============================
       matricula = matricula.replace(" ", "").replace("-", "").upper()

       patron = r"^[0-9]{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$"
       if not re.match(patron, matricula):
        return False, "Formato de matrícula no válido (Ej: 1234BCD)"

    # =============================
    # VALIDAR AÑO
    # =============================
       if not anio.isdigit() or not (1900 <= int(anio) <= 2050):
        return False, "Año no válido"

    # =============================
    # VALIDAR CONSUMO
    # =============================
       try:
        cons = float(consumo)
        if cons <= 0:
            return False, "El consumo debe ser mayor que 0"
       except:
        return False, "Consumo debe ser numérico"

       return True, "OK"
