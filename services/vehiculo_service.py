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

    # Convertir a mayúsculas automáticamente
       matricula = matricula.upper()

    # MATRÍCULA → 4 números + guion + 3 letras
       patron = r"^\d{4}-[A-Z]{3}$"

       if not re.match(patron, matricula):
        return False, "Formato de matrícula inválido (ej: 1234-ABC)"

    # AÑO → 4 dígitos
       if not anio.isdigit() or len(anio) != 4:
        return False, "Año inválido"

    # CONSUMO → número válido
       try:
          consumo_f = float(consumo)
          if consumo_f <= 0:
            return False, "Consumo debe ser mayor que 0"
       except:
        return False, "Consumo debe ser numérico"

       return True, "OK"