import flet as ft

class MiAppBar:
    def __init__(self,page, titulo="Mi App"):
        self.page = page
        self.app_bar = ft.AppBar(
            title=ft.Text(titulo),
            center_title=True,
            bgcolor=ft.colors.BLUE_600,
            actions=[
                ft.IconButton(icon=ft.icons.HOME, on_click=self.volver_inicio),
                ft.IconButton(icon=ft.icons.LOGOUT, on_click=self.cerrar_sesion)
            ]
        )

    def volver_inicio(self, e):
        print("Volver al inicio")  # Aquí podrías usar navegación
        from inicio import contInicial
        contInicial(self.page)
    def cerrar_sesion(self, e):
        print("Cerrar sesión")  # Aquí podrías limpiar sesión y redirigir

    def obtener(self):
        return self.app_bar
