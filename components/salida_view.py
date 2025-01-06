import flet as ft
from database import registrar_salida

def Salida_view(page, app_state):
    # Función que se ejecuta al hacer clic en el botón
    def button_click(e):
        patente_val = patente.value

        # Validar que se haya ingresado la patente
        if not patente_val:
            snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, ingresa la patente."),
                action="Cerrar",
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
            return

        # Intentar registrar la salida
        try:
            resultado = registrar_salida(patente_val)  # Función hipotética que maneja la lógica de salida

            if resultado:
                snack_bar = ft.SnackBar(
                    content=ft.Text(f"Salida registrada para la patente: {patente_val}."),
                    action="Cerrar",
                )
            else:
                snack_bar = ft.SnackBar(
                    content=ft.Text("No se encontró un vehículo con esa patente."),
                    action="Cerrar",
                )

            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

            # Limpiar el campo de entrada
            patente.value = ""
            page.update()

        except Exception as error:
            snack_bar = ft.SnackBar(
                content=ft.Text(f"Error al registrar la salida: {str(error)}"),
                action="Cerrar",
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    # Campo de entrada para la patente y botón de acción
    patente = ft.TextField(label="Patente", width=300, bgcolor="white", color="black")
    b = ft.ElevatedButton(
        text="Registrar Salida", 
        on_click=button_click, 
        width=150, 
        bgcolor="white", 
        color="black"
    )

    # Retornar el formulario en un contenedor
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
