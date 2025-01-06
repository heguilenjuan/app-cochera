import flet as ft
from .registro_view import DataTable
from .ingreso_view import Entrada_view
from .salida_view import Salida_view
from .panel_admin_view import Panel_admin

def Tabs_view(page:ft.Page, app_state):    
    return ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Registro",
                icon=ft.Icons.CARD_MEMBERSHIP,
                content=DataTable(page, app_state),
            ),
            ft.Tab(
                text="Ingreso",
                icon=ft.Icons.CAR_RENTAL,
                content=Entrada_view(page,app_state),
            ),
            ft.Tab(
                text="Salida",
                icon=ft.Icons.EXIT_TO_APP,
                content=Salida_view(page, app_state)
            ),
            ft.Tab(
                text="Administrar",
                icon=ft.Icons.EDIT,
                content=Panel_admin(page,app_state)
            )
        ],
        expand=1
    )
