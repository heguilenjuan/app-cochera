import flet as ft
from database import insertar_auto, insertar_registro

def Entrada_view(page: ft.Page):

    def button_click(e):
        patente_val = patente.value
        tipo_val = tipo.value
        
        if not patente_val or not tipo_val:
            print("completa todos los campos.")
            return 
        
        # Insertar auto y registrar entrada
        insertar_auto(patente_val, tipo_val)
        insertar_registro(patente_val)
        
        # Crear un Snackbar
        snack_bar = ft.SnackBar(
            content=ft.Text(f"Ingreso el auto {patente_val} exitosamente."),
            action="Cerrar",
        )
        
        # Agregar el Snackbar al overlay de la página
        page.overlay.append(snack_bar)
        snack_bar.open = True  # Abrimos el snackbar
        page.update()  # Aseguramos que la página se actualice para mostrar el snackbar
    
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
