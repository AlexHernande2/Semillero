import flet as ft

def home_view(page: ft.Page):
    def ir_a_pagina_datUsuario(evento):
        page.go("/datos_usuario")
    
    titulo = ft.Text("Cultura de Tunja",
                     size=30,
                     text_align=ft.TextAlign.CENTER, 
                     width=page.width)
    
    imagenPrin = ft.Image(
        src="https://static.vecteezy.com/system/resources/previews/024/553/630/non_2x/colorful-owl-pop-art-style-owl-sticker-pastel-cute-colors-ai-generated-png.png",
        fit="contain",
        width=300,
        height=300)
    
    boton_iniciar = ft.ElevatedButton(
        "Bienvenido",
        on_click=ir_a_pagina_datUsuario,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=10)
        ))
    
    contenido = ft.Column(
        controls=[
            ft.Container(
                content=titulo,
                alignment=ft.alignment.top_center,
                margin=ft.margin.only(bottom=20)),
            ft.Container(
                content=imagenPrin,
                alignment=ft.alignment.center,
                expand=True),
            ft.Container(
                content=boton_iniciar,
                alignment=ft.alignment.bottom_center,
                margin=ft.margin.only(top=20))
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True)
    
    return ft.View(
        "/",
        controls=[
            ft.Container(
                content=contenido,
                expand=True,
                alignment=ft.alignment.center)
        ])