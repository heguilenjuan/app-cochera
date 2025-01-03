import flet as ft
from .registro_view import DataTable


def Tabs_view():    
    return ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Registro",
                icon=ft.Icons.CARD_MEMBERSHIP,
                content=DataTable(),
            ),
            ft.Tab(
                text="Ingreso",
                icon=ft.Icons.CAR_RENTAL,
                content=ft.Text("Esta es la pestaña Ingreso")
            ),
            ft.Tab(
                text="Salida",
                icon=ft.Icons.EXIT_TO_APP,
                content=ft.Text("Esta es la pestaña Salida")
            )
        ],
        expand=1
    )
