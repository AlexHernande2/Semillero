import flet as ft


class MiAppBar:
    def __init__(
        self,
        page: ft.Page,
        titulo: str = "Mi App",
        actions: list[ft.Control] | None = None,
        # bgcolor: ft.Colors | None = None, ##CC2B52
        bgcolor: str="#CC2B52",
        titulo_color: str = "#000000",
        titulo_size: float = 20,
        titulo_weight: ft.FontWeight = ft.FontWeight.NORMAL,
        mostrar_volver: bool = False   # Volver atrás
    ):
        self.page = page
        
        volver_btn = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=ft.colors.WHITE,
            on_click=self.volver_atras
        ) if mostrar_volver else None
        

        self.app_bar = ft.AppBar(
            title=ft.Text(
                titulo,
                color=titulo_color,    # color del texto
                size=titulo_size,      # tamaño de la fuente
                weight=titulo_weight
                          
            ),
            center_title=True,
            bgcolor=bgcolor or ft.colors.BLUE_600,
            actions=actions or [],
            leading=volver_btn
        )

    def volver_atras(self, e):
        # self.route.view_pop(None) 
        #manejar con captura de ruta para los parametros
        self.page.go("/")  # vuelve a la vista anterior en el historial
        print("Click atrás")
    


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
