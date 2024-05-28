from excepciones import TicketError
from consulta import Consulta
from socio import Socio

class Ticket:
    def __init__(self, consulta, socio, numero):
        if not isinstance(consulta, Consulta):
            raise TicketError("La consulta debe ser un objeto Consulta.")
        if not isinstance(socio, Socio):
            raise TicketError("El socio debe ser un objeto Socio.")
        if not (1 <= numero <= consulta.max_pacientes):
            raise TicketError("Número de consulta no válido.")
        if numero in [p[1] for p in consulta.pacientes]:
            raise TicketError("Este número de consulta ya está ocupado.")
        
        self.consulta = consulta
        self.socio = socio
        self.numero = numero
        self.precio_final = socio.aplicar_descuento(consulta.especialidad.precio)
        consulta.agregar_paciente(socio, numero)

    def __str__(self):
        return f"Ticket: Consulta {self.consulta.fecha} con {self.consulta.medico.nombre} {self.consulta.medico.apellido}, Socio: {self.socio.nombre} {self.socio.apellido}, Número: {self.numero}, Precio: ${self.precio_final}"
