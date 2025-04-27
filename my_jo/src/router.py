# router.py
import flet as ft
from datosUsuario import datosUsuario
from formulario import formulario_usuario
from inicio import contInicial
from hTunja import historia
from urllib.parse import parse_qs, urlparse
from functools import partial


class Route: 
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        
        # Diccionario que asocia rutas con funciones
        self.routes = {
            "/": self.load_home,
            "/datos_usuario": partial(datosUsuario, self.page),
            "/inicio": partial(contInicial, self.page),
            "/hTunja": partial(historia, self.page)
        }

        self.route_change()# Cargar la ruta inicial


    def load_home(self):
        from home import home_view
        return home_view(self.page)

    def route_change(self, event=None):
        self.page.views.clear()
        print("Ruta actual:", self.page.route)

        # Manejar rutas con parámetros (por ejemplo, formulario_usuario?ced=123)
        if self.page.route.startswith("/formulario_usuario"):
            query_params = parse_qs(urlparse(self.page.route).query)
            ced = query_params.get("ced", [""])[0]
            self.page.views.append(formulario_usuario(self.page, ced))
        
        else:
            # Buscar la vista en el diccionario
            view_builder = self.routes.get(self.page.route)
            if view_builder:
                self.page.views.append(view_builder())
            else:
                # Mostrar vista 404 si no encuentra la ruta
                self.page.views.append(self.error_404())

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


    def error_404(self):
        return ft.View(
            "/404",
            controls=[
                ft.Text("404 - Página no encontrada", size=30, weight="bold"),
                ft.ElevatedButton("Volver al Inicio", on_click=lambda _: self.page.go("/"))
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )




    # def route_change(self, event=None):
    #     self.page.views.clear()
    #     print("Ruta actual:", self.page.route)
        
    #     if self.page.route == "/":
    #         from home import home_view
    #         self.page.views.append(home_view(self.page))
        
    #     elif self.page.route == "/datos_usuario":
    #         self.page.views.append(datosUsuario(self.page))
    #         self.page.update()
        
    #     elif self.page.route == "/inicio":
    #         self.page.views.append(contInicial(self.page))
        
    #     elif self.page.route.startswith("/formulario_usuario"):
    #         query_params = parse_qs(urlparse(self.page.route).query)
    #         ced = query_params.get("ced", [""])[0]
    #         self.page.views.append(formulario_usuario(self.page, ced))
        
    #     self.page.update()

    # def view_pop(self, view):
    #     self.page.views.pop()
    #     top_view = self.page.views[-1]
    #     self.page.go(top_view.route)


    # def view_pop(self, view):
    #     if len(self.page.views) > 1:
    #         self.page.views.pop()
    #         top_view = self.page.views[-1]
    #         self.page.route = top_view.route  # Actualiza la ruta
    #         self.page.update()  # Fuerza la actualización