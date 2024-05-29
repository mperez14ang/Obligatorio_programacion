from Exceptions.excepciones import MedicoError
from datetime import date

class Medico:
    def __init__(self, nombre: str, apellido: str, cedula: str, fecha_nacimiento: date, fecha_ingreso: date, celular: str, especialidad: str):
        if not isinstance(nombre, str) or len(nombre) == 0:
            raise MedicoError("No es un nombre válido, ingréselo de nuevo.")
        if not isinstance(apellido, str) or len(apellido) == 0:
            raise MedicoError("No es un apellido válido, ingréselo de nuevo.")
        if not cedula.isdigit() or len(cedula) != 8:
            raise MedicoError("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        if not celular.isdigit() or len(celular) != 9:
            raise MedicoError("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        if not isinstance(fecha_nacimiento, date) or not isinstance(fecha_ingreso, date):
            raise MedicoError("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        if not isinstance(especialidad, str):
            raise MedicoError("La especialidad debe ser un string.")
        
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular
        self.especialidad = especialidad

    def __str__(self) -> str:
        return f"Dr. {self.nombre} {self.apellido}, Especialidad: {self.especialidad}"
