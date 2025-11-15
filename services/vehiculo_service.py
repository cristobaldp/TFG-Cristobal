import json

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
        if len(matricula) < 4:
            return False, "Matrícula demasiado corta"
        if not anio.isdigit():
            return False, "Año no válido"
        try:
            consumo = float(consumo)
            if consumo <= 0:
                return False, "Consumo inválido"
        except:
            return False, "Consumo debe ser numérico"
        return True, "OK"
