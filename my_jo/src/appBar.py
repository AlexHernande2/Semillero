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
        mostrar_volver: bool = False,   # Volver atrás
        mostrar_menu : bool = False
    ):
        self.page = page
        
        self.volver_btn = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            on_click=self.volver_atras
        ) if mostrar_volver else None

        #Boton menu lateral

        self.menu_btn =ft.IconButton(
            icon=ft.Icons.MENU,
            icon_color=ft.Colors.WHITE,
            on_click=self.abrir_menu 
        )if mostrar_menu else None
        


        # Drawer (menú lateral)
        if  mostrar_menu:
            self.page.drawer = ft.NavigationDrawer(
                controls=[
                    ft.Container(
                        content=ft.Text("Menú principal", size=20, weight=ft.FontWeight.BOLD),
                        padding=10
                    ),
                    ft.Divider(),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.HOME),
                        title=ft.Text("Inicio"),
                        on_click=self.volver_inicio
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.HISTORY),
                        title=ft.Text("Historia de Tunja"),
                        on_click=lambda e: self.page.go("/hTunja")
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.LOGOUT),
                        title=ft.Text("Cerrar sesión"),
                        on_click=self.cerrar_sesion
                    )
                ]
            )

            # Construcción del AppBar
        self.app_bar = ft.AppBar(
            title=ft.Text(
                titulo,
                color=titulo_color,    # color del texto
                size=titulo_size,      # tamaño de la fuente
                weight=titulo_weight
                          
            ),
            center_title=True,
            bgcolor=bgcolor or ft.Colors.BLUE_600,
            leading=self.volver_btn,
            actions=(
                [self.menu_btn] if self.menu_btn else []
            ) + (actions or [])  # Botón de menú a la derecha (si existe,
            
        )


    def abrir_menu(self, e):
        self.page.drawer.open = True
        self.page.drawer.update()
    

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
