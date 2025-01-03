import sqlite3
from datetime import datetime

class Registro:
    def __init__(self, patente, hora_entrada, hora_salida=None, total=None):
        self.patente = patente
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.total = total

    def guardar(self):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patente TEXT,
                hora_entrada TEXT,
                hora_salida TEXT,
                total REAL,
                FOREIGN KEY (patente) REFERENCES autos (patente)
            )
        """)

        cursor.execute("""
            INSERT INTO registros (patente, hora_entrada, hora_salida, total)
            VALUES (?, ?, ?, ?)
        """, (self.patente, self.hora_entrada, self.hora_salida, self.total))

        conn.commit()
        conn.close()

    @classmethod
    def obtener_registro(cls, id_registro):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM registros WHERE id = ?
        """, (id_registro,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return cls(patente=result[1], hora_entrada=result[2], hora_salida=result[3], total=result[4])
        return None

    @classmethod
    def obtener_todos(cls):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM registros
        """)
        registros = cursor.fetchall()
        conn.close()

        # Devolver una lista de objetos Registro
        return [cls(patente=r[1], hora_entrada=r[2], hora_salida=r[3], total=r[4]) for r in registros]

    def calcular_total(self, tarifa_por_hora):
        if self.hora_salida:
            entrada = datetime.strptime(self.hora_entrada, '%Y-%m-%d %H:%M:%S')
            salida = datetime.strptime(self.hora_salida, '%Y-%m-%d %H:%M:%S')
            tiempo_estacionado = (salida - entrada).total_seconds() / 3600  # Convertir a horas
            self.total = tiempo_estacionado * tarifa_por_hora
        return self.total
