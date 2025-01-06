import sqlite3

class Tarifa:
    def __init__(self, tarifa_por_hora):
        self.tarifa_por_hora = tarifa_por_hora

    def guardar(self):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarifas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarifa_por_hora REAL
            )
        """)
        
        cursor.execute("""
            INSERT INTO tarifas (tarifa_por_hora) 
            VALUES (?)
        """, (self.tarifa_por_hora,))
        
        conn.commit()
        conn.close()

    @classmethod
    def obtener_tarifa(cls):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT tarifa_por_hora FROM tarifas ORDER BY id DESC LIMIT 1
        """)
        result = cursor.fetchone()
        conn.close()

        if result:
            return cls(tarifa_por_hora=result[0])
        return None
    @classmethod
    def obtener_todas(cls):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM tarifas
        """)
        
        resultados = cursor.fetchall()
        conn.close()
        
        #devolver una lista de objetos Tarifa
        return[cls(id=row[0], tarifas_por_hora=row[1]) for row in resultados]
    
    @classmethod
    def actualizar(cls, id_tarifa, nueva_tarifa):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE tarifas
            SET tarifas_por_hora = ?
            WHERE id = ?
        """,(nueva_tarifa, id_tarifa))
        
        conn.commit()
        conn.close()
        
    @classmethod
    def eliminar(cls, id_tarifa):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM tarifas WHERE id = ?
        """, (id_tarifa))
        
        conn.commit()
        conn.close()
        