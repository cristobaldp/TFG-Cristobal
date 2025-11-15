class Vehiculo:
    def __init__(self,
                 id=None,
                 marca="",
                 modelo="",
                 matricula="",
                 tipo="",
                 combustible="",
                 consumo=0.0,
                 kilometraje=0,
                 id_usuario=None):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.tipo = tipo
        self.combustible = combustible
        self.consumo = consumo
        self.kilometraje = kilometraje
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "matricula": self.matricula,
            "tipo": self.tipo,
            "combustible": self.combustible,
            "consumo": self.consumo,
            "kilometraje": self.kilometraje,
            "id_usuario": self.id_usuario
        }
