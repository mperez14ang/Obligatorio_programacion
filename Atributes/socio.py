from Exceptions.excepciones import SocioError
from datetime import datetime, date 

class Socio:
    def __init__(self,nombre :str, apellido: str, cedula: str, fecha_nacimiento: date,fecha_ingreso: date, celular: str, tipo: int):
        if not isinstance(nombre, str):
            raise SocioError("No es un nombre válido, ingréselo de nuevo")
        if len(nombre) == 0:
            raise SocioError("No es un nombre válido, ingréselo de nuevo")
        if not isinstance(apellido, str):
            raise SocioError("No es un apellido válido, ingréselo de nuevo")
        if len(apellido) == 0:
            raise SocioError("No es un apellido válido, ingréselo de nuevo")
        if not cedula.isdigit() or len(cedula) != 8:
            raise SocioError("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        if not celular.isdigit() or len(celular) != 9:
            raise SocioError("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
        if not isinstance(fecha_nacimiento, date) or not isinstance(fecha_ingreso, date):
            raise SocioError("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        if tipo not in [1,2]:
            raise SocioError("El valor ingresado no es correcto, elige la opción 1 o 2.")
        
        self.nombre = nombre
        self.apellido = apellido    
        self.cedula = cedula
        self.fecha_nachimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular
        self.tipo = tipo
        self.deuda = 0

        def __str__(self):
             return f"{self.nombre} {self.apellido}, CI: {self.cedula}, Tipo: {'Bonificado' if self.tipo == 1 else 'No Bonificado'}, Deuda: ${self.deuda}"