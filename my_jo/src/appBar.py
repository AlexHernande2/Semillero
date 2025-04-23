import flet as ft

class MiAppBar:
    def __init__(
        self,
        page: ft.Page,
        titulo: str = "Mi App",
        actions: list[ft.Control] | None = None,
        bgcolor: ft.Colors | None = None
    ):
        self.page = page
        self.app_bar = ft.AppBar(
            title=ft.Text(titulo),
            center_title=True,
            bgcolor=bgcolor or ft.colors.BLUE_600,
            actions=actions or []
        )

    def volver_inicio(self, e):
        # tu lógica de “volver al inicio”
        from inicio import contInicial
        contInicial(self.page)

    def cerrar_sesion(self, e):
        # tu lógica de logout
        self.page.session.clear()
        self.page.go("/")

    def obtener(self) -> ft.AppBar:
        return self.app_bar
