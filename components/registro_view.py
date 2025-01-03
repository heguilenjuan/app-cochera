import flet as ft
from models.registro import Registro

def DataTable (page:ft.Page):
    registros = Registro.obtener_todos()
    
    #crea las filas de la tabla en base a los registros
    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(registro.patente)),
            ft.DataCell(ft.Text(registro.hora_entrada)),
            ft.DataCell(ft.Text(registro.hora_salida)),
            ft.DataCell(ft.Text(registro.total)),
        ]) for registro in registros
    ]
    table = ft.DataTable(
        vertical_lines= ft.BorderSide(1, "white"),
        horizontal_lines=ft.BorderSide(1, "white"),
        columns=[
            ft.DataColumn(ft.Text("Patente")),
            ft.DataColumn(ft.Text("Hora de Entrada")),
            ft.DataColumn(ft.Text("Hora de Salida")),
            ft.DataColumn(ft.Text("Total")), 
        ],
        rows=rows,
    )
    return table