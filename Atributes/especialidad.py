from Exceptions.excepciones import EspecialidadError

class Especialidad:
    def __init__(self, nombre: str, precio: int):
        if type(nombre) != str:
            raise EspecialidadError("El nombre de la especialidad debe ser un string")
        if len(nombre) == 0:
            raise EspecialidadError("El nombre de la especialidad no puede ser vacío")
        self.nombre = nombre
        if type(precio) != int:
            raise EspecialidadError("El precio de la especialidad debe ser un entero")
        if precio < 0:
            raise EspecialidadError("El precio de la especialidad no puede ser negativo")
        
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Especialidad: {self.nombre}, Precio: ${self.precio}"