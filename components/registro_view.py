import flet as ft
from models.registro import Registro

def DataTable(page: ft.Page, app_state):
    # Función para actualizar la tabla
    def actualizar_tabla():
        # Obtener todos los registros
        registros = Registro.obtener_todos()

        # Limpiar las filas existentes
        table.rows.clear()

        if not registros:
            # Si no hay registros, agregar un mensaje de "No hay registros"
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("No hay registros cargados")),
                        ft.DataCell(),
                        ft.DataCell(),
                        ft.DataCell(),
                    ]
                )
            )
        else:
            # Crear filas para cada registro
            table.rows.extend([
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(registro.patente)),
                    ft.DataCell(ft.Text(registro.hora_entrada)),
                    ft.DataCell(ft.Text(registro.hora_salida)),
                    ft.DataCell(ft.Text(str(registro.total))),
                ])
                for registro in registros
            ])
        page.update()

    # Crear la tabla inicialmente
    table = ft.DataTable(
        vertical_lines=ft.BorderSide(1, "white"),
        horizontal_lines=ft.BorderSide(1, "white"),
        columns=[
            ft.DataColumn(ft.Text("Patente")),
            ft.DataColumn(ft.Text("Hora de Entrada")),
            ft.DataColumn(ft.Text("Hora de Salida")),
            ft.DataColumn(ft.Text("Total")),
        ],
    )

    # Inicializar la tabla con datos actuales
    actualizar_tabla()

    return table
