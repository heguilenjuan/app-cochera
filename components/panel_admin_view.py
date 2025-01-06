import flet as ft
from models.tarifas import Tarifa

def Panel_admin(page: ft.Page, app_state):
    # Función para modificar la tarifa
    def modificar_tarifa(e, id, tipo, nueva):
        if nueva:  # Asegurarse de que hay un nuevo valor
            Tarifa.actualizar(id, tipo, nueva)
            print(f"Tarifa {id} actualizada a {nueva}")
            page.dialog.open = False  # Cerrar el diálogo
            actualizar_tabla()  # Actualizar la tabla
            page.update()

    # Función para eliminar la tarifa
    def eliminar_tarifa(e, id):
        # Crear el diálogo de confirmación de eliminación
        confirm = ft.AlertDialog(
            title=ft.Text("¿Estás seguro de que quieres eliminar esta tarifa?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: cerrar_dialogo()),
                ft.TextButton("Eliminar", on_click=lambda _: confirmar_eliminar(id)),
            ],
        )
        page.dialog = confirm
        page.dialog.open = True
        page.update()

    # Función para confirmar la eliminación
    def confirmar_eliminar(id):
        Tarifa.eliminar(id)
        print(f"Tarifa {id} eliminada")
        cerrar_dialogo()
        actualizar_tabla()  # Actualizar la tabla

    # Función para cerrar cualquier diálogo
    def cerrar_dialogo():
        page.dialog.open = False
        page.update()

    # Función para editar la tarifa
    def editar_tarifa(e, id, tipo):
        new_value_input = ft.TextField(label="Nuevo valor", autofocus=True)
        edit_dialog = ft.AlertDialog(
            title=ft.Text(f"Modificar tarifa {id}"),
            content=new_value_input,
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: cerrar_dialogo()),
                ft.TextButton(
                    "Aceptar",
                    on_click=lambda _: modificar_tarifa(None, id, tipo, new_value_input.value),
                ),
            ],
        )
        page.dialog = edit_dialog
        page.dialog.open = True
        page.update()

    # Función para actualizar la tabla
    def actualizar_tabla():
        tarifas = Tarifa.obtener_todas()
        table.rows.clear()  # Limpiar las filas actuales
        if tarifas:
            table.rows.extend([
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(tarifa.id))),
                    ft.DataCell(ft.Text(tarifa.tipo)),
                    ft.DataCell(ft.Text(str(tarifa.tarifa_por_hora))),
                    ft.DataCell(
                        ft.Row(
                            [
                                ft.IconButton(
                                    ft.Icons.EDIT,
                                    icon_color="yellow",
                                    on_click=lambda e, id=tarifa.id, tipo=tarifa.tipo: editar_tarifa(e, id, tipo),
                                ),
                                ft.IconButton(
                                    ft.Icons.DELETE,
                                    icon_color="red",
                                    on_click=lambda e, id=tarifa.id: eliminar_tarifa(e, id),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ),
                ])
                for tarifa in tarifas
            ])
        else:
            table.rows.append(
                ft.DataRow(cells=[ft.DataCell(ft.Text("No hay tarifas cargadas")), ft.DataCell(), ft.DataCell(), ft.DataCell()])
            )
        page.update()

    # Crear la tabla inicialmente
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Precio x Hora")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
    )
    actualizar_tabla()  # Llenar la tabla con datos iniciales

    return table
