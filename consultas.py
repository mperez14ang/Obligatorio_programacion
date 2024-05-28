from medico import Medico
from socio import Socio
from consulta import Consulta
from datetime import datetime

def obtener_medicos_por_especialidad(medicos, especialidad_nombre):
    return [medico for medico in medicos if medico.especialidad.nombre == especialidad_nombre]

def obtener_precio_por_especialidad(especialidades, especialidad_nombre):
    for especialidad in especialidades:
        if especialidad.nombre == especialidad_nombre:
            return especialidad.precio
    return None

def listar_socios_con_deudas(socios):
    return sorted(socios, key=lambda socio: socio.deuda)

def consultas_entre_fechas(consultas, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    return [consulta for consulta in consultas if fecha_inicio <= datetime.strptime(consulta.fecha, '%Y-%m-%d') <= fecha_fin]

def ganancias_entre_fechas(tickets, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    return sum(ticket.precio_final for ticket in tickets if fecha_inicio <= datetime.strptime(ticket.consulta.fecha, '%Y-%m-%d') <= fecha_fin)
