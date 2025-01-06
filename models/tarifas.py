import sqlite3

class Tarifa:
    def __init__(self, tipo, tarifa_por_hora, id=None):
        self.id = id
        self.tipo = tipo
        self.tarifa_por_hora = tarifa_por_hora

    @staticmethod
    def crear_tabla():
        # Crea la tabla tarifas si no existe
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarifas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT,
                tarifa_por_hora REAL
            )
        """)
            
        conn.commit()
        conn.close()

    def guardar(self):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tarifas (tipo, tarifa_por_hora) 
            VALUES (?, ?)
        """, (self.tipo, self.tarifa_por_hora))

        conn.commit()
        conn.close()

    @classmethod
    def obtener_todas(cls):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tarifas
        """)

        resultados = cursor.fetchall()
        conn.close()

        # devolver una lista de objetos Tarifa
        return [cls(id=row[0], tipo=row[1], tarifa_por_hora=row[2]) for row in resultados]

    @classmethod
    def actualizar(cls, id_tarifa, tipo_tarifa, nueva_tarifa):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tarifas
            SET tipo = ?, tarifa_por_hora = ?
            WHERE id = ?
        """, (tipo_tarifa, nueva_tarifa, id_tarifa))

        conn.commit()
        conn.close()

    @classmethod
    def eliminar(cls, id_tarifa):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM tarifas WHERE id = ?
        """, (id_tarifa,))

        conn.commit()
        conn.close()
        

