import flet as ft 
from appBar import MiAppBar

#Esta clase va ser para mostrar solo datos relacionados con Tunja
def historia(page: ft.Page):
    page.tittle = "Historia de Tunja"

    appbar = MiAppBar (
        page, 
        titulo= "Historía de Tunja",
        bgcolor="#CC2B52",
        actions=[],        
        titulo_size=28,                              # tamaño de fuente
        titulo_weight=ft.FontWeight.BOLD,               #negrilla
        mostrar_volver=True 

    ).obtener()

    return ft.View(
        "/hTunja",
        appbar=appbar
        # controls=[
        #     ft.Container(
        #         content=gestos,
        #         alignment=ft.alignment.center,
        #         expand=True
        #     )
        # ]
    )
