from models.auto import Auto
from models.registro import Registro
from models.tarifas import Tarifa
from datetime import datetime

def insertar_auto(patente, tipo):
    auto = Auto(patente, tipo)
    auto.guardar()

def insertar_registro(patente):
    # Registrar la hora de entrada
    hora_entrada = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    registro = Registro(patente, hora_entrada)
    registro.guardar()

def registrar_salida(id_registro, hora_salida):
    # Obtener el registro y calcular el total
    tarifa = Tarifa.obtener_tarifa()
    if tarifa:
        registro = Registro.obtener_registro(id_registro)
        if registro:
            registro.hora_salida = hora_salida
            total = registro.calcular_total(tarifa.tarifa_por_hora)
            registro.total = total
            registro.guardar()
            return registro.total
    return None
