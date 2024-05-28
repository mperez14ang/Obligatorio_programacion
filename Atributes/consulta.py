from Exceptions.excepciones import ConsultaError
from datetime import date

class Consulta:
    def __init__(self, especialidad: str, medico: str, fecha: date, max_pacientes: int):
        if not isinstance(especialidad, str):
            raise ConsultaError("La especialidad debe ser un string.")
        if not isinstance(medico, str):
            raise ConsultaError("El nombre del médico debe ser un string.")
        if not isinstance(max_pacientes, int) or max_pacientes <= 0:
            raise ConsultaError("La cantidad máxima de pacientes debe ser un número entero positivo.")
        
        self.especialidad = especialidad
        self.medico = medico
        self.fecha = fecha
        self.max_pacientes = max_pacientes
        self.pacientes = []

        def agregar_paciente(self, paciente: str, numero: int):
            if len(self.pacientes) < self.max_pacientes and numero <= self.max_pacientes:
                self.pacientes.insert(numero -1 , paciente)
            else:
                raise ConsultaError("No se puede agregar más pacientes a la consulta. o numero invalido")
        
        def __str__(self) -> str:
            return f"Consulta de {self.especialidad} con {self.medico} el {self.fecha}, Maximo pacientes: {self.max_pacientes}"
        