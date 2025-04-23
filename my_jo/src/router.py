# router.py
import flet as ft
from datosUsuario import datosUsuario
from formulario import formulario_usuario
from inicio import contInicial
from urllib.parse import parse_qs, urlparse

class Route: 
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.route_change()  # Cargar la ruta inicial

    def route_change(self, event=None):
        self.page.views.clear()
        print("Ruta actual:", self.page.route)
        
        if self.page.route == "/":
            from home import home_view
            self.page.views.append(home_view(self.page))
        
        elif self.page.route == "/datos_usuario":
            self.page.views.append(datosUsuario(self.page))
            self.page.update()
        
        elif self.page.route == "/inicio":
            self.page.views.append(contInicial(self.page))
        
        elif self.page.route.startswith("/formulario_usuario"):
            query_params = parse_qs(urlparse(self.page.route).query)
            ced = query_params.get("ced", [""])[0]
            self.page.views.append(formulario_usuario(self.page, ced))
        
        self.page.update()

    # def view_pop(self, view):
    #     self.page.views.pop()
    #     top_view = self.page.views[-1]
    #     self.page.go(top_view.route)
    def view_pop(self, view):
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.route = top_view.route  # Actualiza la ruta
            self.page.update()  # Fuerza la actualización