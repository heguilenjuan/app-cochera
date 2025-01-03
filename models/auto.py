import sqlite3

class Auto:
    def __init__(self, patente, tipo):
        self.patente = patente
        self.tipo = tipo

    def guardar(self):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        # Corregir el error en la definición de la tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autos (
                patente TEXT PRIMARY KEY,
                tipo TEXT
            )
        """)
        
        # Realizar el insert
        cursor.execute("""
            INSERT OR REPLACE INTO autos (patente, tipo) 
            VALUES (?, ?)
        """, (self.patente, self.tipo))
        
        conn.commit()
        conn.close()

    @classmethod
    def obtener_auto(cls, patente):
        conn = sqlite3.connect('cochera.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM autos WHERE patente = ?
        """, (patente,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return cls(patente=result[0], tipo=result[1])
        return None
