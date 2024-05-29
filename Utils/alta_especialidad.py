from Entities.especialidad import Especialidad
from Exceptions.excepciones import EspecialidadError

def alta_especialidad():
    while True:
        try:
            nombre = input("Ingrese el nombre de la especialidad: ")
            if not isinstance(nombre, str) or not nombre.strip():
                raise EspecialidadError("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
            
            precio_str = input("Ingrese el precio asociado: ")
            if not precio_str.isdigit() or int(precio_str) < 0:
                raise EspecialidadError("El precio de la especialidad es incorrecto, ingréselo nuevamente.")
            
            precio = int(precio_str)
            
            # Crear una instancia de Especialidad
            especialidad = Especialidad(nombre, precio)
            
            print("La especialidad se ha creado con éxito")
            break
        except EspecialidadError as e:
            print(e)
        except ValueError:
            print("El precio de la especialidad es incorrecto, ingréselo nuevamente.")


