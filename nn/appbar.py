import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Ejemplo de AppBar con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Crear la AppBar
    app_bar = ft.AppBar(
        title=ft.Text("Mi AppBar"),
        actions=[
            ft.IconButton(ft.icons.ADD, tooltip="Agregar"),
            ft.IconButton(ft.icons.SEARCH, tooltip="Buscar"),
            ft.IconButton(ft.icons.SETTINGS, tooltip="Configuraciones"),
        ],
    )

    # Contenido de la página
    content = ft.Column(
        [
            ft.Text("¡Bienvenido a mi aplicación!"),
            ft.Text("Aquí puedes agregar más contenido."),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Agregar la AppBar y el contenido a la página
    page.add(app_bar, content)

# Ejecutar la aplicación
ft.app(target=main)