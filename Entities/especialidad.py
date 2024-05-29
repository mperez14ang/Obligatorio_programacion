class Especialidad:
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Especialidad: {self.nombre}, Precio: ${self.precio}"
