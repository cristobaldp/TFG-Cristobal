class CitiesService:
    def __init__(self, file_path="data/ciudades.txt"):
        self.file_path = file_path

    def cargar(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return [c.strip() for c in f.readlines() if c.strip()]
        except:
            return []
