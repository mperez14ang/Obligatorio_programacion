from excepciones import ConsultaError
from especialidad import Especialidad
from medico import Medico
from datetime import datetime
from socio import Socio

class Consulta:
    def __init__(self, especialidad, medico, fecha, max_pacientes):
        if not isinstance(especialidad, Especialidad):
            raise ConsultaError("La especialidad debe ser un objeto Especialidad.")
        if not isinstance(medico, Medico):
            raise ConsultaError("El médico debe ser un objeto Medico.")
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            raise ConsultaError("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        if not isinstance(max_pacientes, int) or max_pacientes <= 0:
            raise ConsultaError("La cantidad de pacientes debe ser un entero positivo.")

        self.especialidad = especialidad
        self.medico = medico
        self.fecha = fecha
        self.max_pacientes = max_pacientes
        self.pacientes = []

    def agregar_paciente(self, socio, numero):
        if not isinstance(socio, Socio):
            raise ConsultaError("El paciente debe ser un objeto Socio.")
        if not (1 <= numero <= self.max_pacientes):
            raise ConsultaError("Número de consulta no válido.")
        if numero in [p[1] for p in self.pacientes]:
            raise ConsultaError("Este número de consulta ya está ocupado.")

        self.pacientes.append((socio, numero))

    def __str__(self):
        return f"Consulta: {self.fecha}, Médico: {self.medico.nombre} {self.medico.apellido}, Especialidad: {self.especialidad.nombre}, Pacientes: {len(self.pacientes)}/{self.max_pacientes}"

