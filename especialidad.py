from excepciones import EspecialidadError

class Especialidad:
    def __init__(self, nombre, precio):
        if not isinstance(nombre, str):
            raise EspecialidadError("El nombre de la especialidad debe ser un string.")
        if not isinstance(precio, int):
            raise EspecialidadError("El precio de la especialidad debe ser un entero.")
        
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Especialidad: {self.nombre}, Precio: ${self.precio}"
