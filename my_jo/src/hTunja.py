import flet as ft 
from appBar import MiAppBar

#Esta clase va ser para mostrar solo datos relacionados con Tunja
def historia(page: ft.Page):
    page.title = "Historia de Tunja"

    mi_appbar = MiAppBar (
        page, 
        titulo= "Historía de Tunja",
        bgcolor="#CC2B52",
        # actions=[],        
        titulo_size=28,                              # tamaño de fuente
        titulo_weight=ft.FontWeight.BOLD,               #negrilla
        mostrar_volver=True,
        mostrar_menu= True

    )
    appbar= mi_appbar.obtener()
    
    



    return ft.View(
        "/hTunja",
        appbar=appbar,
        drawer=page.drawer, 
        # controls=[
        #     ft.Container(
        #         content=gestos,
        #         alignment=ft.alignment.center,
        #         expand=True
        #     )
        # ]
    )
