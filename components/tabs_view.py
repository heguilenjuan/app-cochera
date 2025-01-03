import flet as ft
from .registro_view import DataTable
from .ingreso_view import Entrada_view
from .salida_view import Salida_view

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
                content=Entrada_view(),
            ),
            ft.Tab(
                text="Salida",
                icon=ft.Icons.EXIT_TO_APP,
                content=Salida_view()
            )
        ],
        expand=1
    )
