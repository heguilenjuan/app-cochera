import flet as ft
from datetime import datetime
from database import insertar_auto, insertar_registro

def Entrada_view():

    def button_click(e):
        patente_val = patente.value
        tipo_val = tipo.value
        
        if not patente_val or not tipo_val:
            print("completa todos los campos.")
            return 
    
        #insertar auto y registrar entrada
        insertar_auto(patente_val, tipo_val)
        insertar_registro(patente_val)

        
    # Campos y botón
    patente = ft.TextField(label="Patente", width=300, bgcolor="white", color="black")
    tipo = ft.TextField(label="Tipo", width=300, bgcolor="white", color="black")
    b = ft.ElevatedButton(text="Ingresar", on_click=button_click, width=150, bgcolor="white", color="black")

    # Retornando el formulario en un contenedor
    return ft.Container(
        content=ft.Column(
            controls=[patente, tipo, b],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=400,
        height=300,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
    )
