import flet as ft


def Salida_view():
    
    def button_click(e):
        print("Cargando los datos")

    # Campos y botón
    patente = ft.TextField(label="Patente", width=300, bgcolor="white", color="black")
    b = ft.ElevatedButton(text="Ingresar", on_click=button_click, width=150, bgcolor="white", color="black")

    # Retornando el formulario en un contenedor
    return ft.Container(
        content=ft.Column(
            controls=[patente, b],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=400,
        height=300,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
    )