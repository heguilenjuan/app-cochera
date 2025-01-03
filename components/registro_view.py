import flet as ft

def DataTable ():
    return ft.DataTable(
        vertical_lines= ft.BorderSide(1, "black"),
        horizontal_lines=ft.BorderSide(1,"black"),
        columns=[
            ft.DataColumn(ft.Text("Patente")),
            ft.DataColumn(ft.Text("Hora de Entrada")),
            ft.DataColumn(ft.Text("Hora de Salida")),
            ft.DataColumn(ft.Text("Estado")),
            ft.DataColumn(ft.Text("Total")), 
        ],
        rows=[
            
        ]
    )