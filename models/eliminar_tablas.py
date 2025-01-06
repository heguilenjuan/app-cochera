import sqlite3

def eliminar_tablas():
    conn = sqlite3.connect('cochera.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM autos
    """)
    cursor.execute("""
        DELETE FROM registros
    """)
    cursor.execute("""
        DELETE FROM tarifas
    """)
    
    conn.commit()
    conn.close()
    
    
eliminar_tablas()