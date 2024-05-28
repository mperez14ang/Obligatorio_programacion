from datetime import datetime
from excepciones import SocioError

class Socio:
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo_socio):
        if not isinstance(nombre, str):
            raise SocioError("No es un nombre válido, ingréselo de nuevo.")
        if not isinstance(apellido, str):
            raise SocioError("No es un apellido válido, ingréselo de nuevo.")
        if not isinstance(cedula, str) or len(cedula) != 8:
            raise SocioError("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        try:
            datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        except ValueError:
            raise SocioError("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        if not (isinstance(celular, str) and len(celular) == 9 and celular.startswith('09')):
            raise SocioError("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        if tipo_socio not in [1, 2]:
            raise SocioError("El valor ingresado no es correcto, elige la opción 1 o 2.")

        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular
        self.tipo_socio = tipo_socio
        self.deuda = 0

    def aplicar_descuento(self, monto):
        if self.tipo_socio == 1:
            return monto * 0.8
        return monto

    def __str__(self):
        return f"Socio: {self.nombre} {self.apellido}, Cédula: {self.cedula}, Tipo: {'Bonificado' if self.tipo_socio == 1 else 'No bonificado'}, Deuda: ${self.deuda}"
