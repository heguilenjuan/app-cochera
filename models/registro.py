from datetime import datetime

class Regitro():
    def __init__(self, auto, tarifa, hora_entrada, hora_salida=None):
        self.auto = auto
        tarifa = tarifa
        hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = "En el lugar" if hora_salida is None else "Retirado"
        self.total = 0
        
    def calcular_total(self):
        if self.hora_salida is None:
            return 0
        #Calcular el tiempo que estuvo estacionado
        tiempo_estacionado = self.hora_salida - self.hora_entrada
        horas_estacionadas = tiempo_estacionado.total_seconds() / 3600 #convierte a horas
        self.total = horas_estacionadas * self.tarifa.tarifa_por_hora
        
        return self.total
    
    def actualizar_salida(self, hora_salida):
        self.hora_salida = hora_salida
        self.estado = "Retirado"
        self.calcular_total()
        
    
        