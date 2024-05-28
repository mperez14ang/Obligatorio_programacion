from excepciones import MedicoError
from datetime import datetime
from especialidad import Especialidad

class Medico:
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad):
        if not isinstance(nombre, str):
            raise MedicoError("No es un nombre válido, ingréselo de nuevo.")
        if not isinstance(apellido, str):
            raise MedicoError("No es un apellido válido, ingréselo de nuevo.")
        if not isinstance(cedula, str) or len(cedula) != 8:
            raise MedicoError("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        try:
            datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        except ValueError:
            raise MedicoError("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        if not (isinstance(celular, str) and len(celular) == 9 and celular.startswith('09')):
            raise MedicoError("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        if not isinstance(especialidad, Especialidad):
            raise MedicoError("La especialidad no es válida.")

        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular
        self.especialidad = especialidad

    def __str__(self):
        return f"Médico: {self.nombre} {self.apellido}, Especialidad: {self.especialidad.nombre}"
