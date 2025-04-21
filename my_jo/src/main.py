import flet as ft
from user_data import init_data
from router import Route

def main(page: ft.Page):
    init_data()
    page.title = "App Cultura"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE

    # Inicializar el enrutador
    Route(page)
    page.go('/')

ft.app(main, view=ft.WEB_BROWSER)