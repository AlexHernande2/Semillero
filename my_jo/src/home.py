import flet as ft
from appBar import MiAppBar

def home_view(page: ft.Page):
    def ir_a_pagina_datUsuario(evento):
        page.go("/datos_usuario")
    
    # titulo = ft.Text("Cultura de Tunja",
    #                  size=30,
    #                  text_align=ft.TextAlign.CENTER, 
    #                  width=page.width)
    
    appbar = MiAppBar(
        page, titulo="Cultura de Tunja",
        bgcolor="#CC2B52",
        actions=[],
                           
        titulo_size=28,                              # tamaño de fuente
        titulo_weight=ft.FontWeight.BOLD               #negrilla
    ).obtener()

    imagenPrin = ft.Image(
        src="https://static.vecteezy.com/system/resources/previews/024/553/630/non_2x/colorful-owl-pop-art-style-owl-sticker-pastel-cute-colors-ai-generated-png.png",
        fit="contain",
        width=300,
        height=300)
    
    boton_iniciar = ft.ElevatedButton(
        "Bienvenido",
        on_click=ir_a_pagina_datUsuario,
        bgcolor="#CC2B52",      # color de fondo
        color="white",          # color del texto
        width=200,              # ancho fijo en píxeles
        height=50               # (opcional) alto fijo
        # expand=True,
        # style=ft.ButtonStyle(
        #     padding=ft.padding.symmetric(horizontal=20, vertical=10)
        # )
    )
    
    contenido = ft.Column(
        controls=[
            # ft.Container(
            #     content=titulo,
            #     alignment=ft.alignment.top_center,
            #     margin=ft.margin.only(bottom=20)),
            ft.Container(
                content=imagenPrin,
                alignment=ft.alignment.center,
                expand=True),
            ft.Container(
                content=boton_iniciar,
                alignment=ft.alignment.center,           # centrar horizontalmente
                margin=ft.margin.only(bottom=20),           # separarlo 20px desde arriba
                padding=ft.padding.symmetric(vertical=5) # un poco de padding interno
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True)
    
    return ft.View(
        "/",
        appbar=appbar,
        controls=[
            ft.Container(
                content=contenido,
                expand=True,
                alignment=ft.alignment.center)
        ])