import flet as ft
from datosIni import datosUsuario


def main(page: ft.Page):
    page.title = "Pagina_Bienvenido"
    page.padding = 20  # Espaciado alrededor del contenido
    
    # Función para navegar a la segunda página
    def ir_a_pagina_inicio(evento):
        datosUsuario(page)  # Llama a la función para cargar la segunda página
      
    titulo = ft.Text("Cultura de Tunja",
                     size=30,
                     text_align=ft.TextAlign.CENTER, 
                     width=page.width              
    )
    # Imagen principal
    imagenPrin = ft.Image(
        src="https://cdn.pixabay.com/photo/2017/05/26/16/08/glass-2346358_1280.png",  # Imagen de ejemplo
        fit="contain",  # La imagen se ajusta al contenedor sin deformarse
        width=300,  # Ancho máximo para la imagen
        height=300  
    )
    # Botón
    boton_iniciar = ft.ElevatedButton(
        "Bienvenido",
        on_click=ir_a_pagina_inicio,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=10)
        ),
    )
    # Estructura del layout
    contenido = ft.Column(
        controls=[
            ft.Container(
                content=titulo,
                alignment=ft.alignment.top_center,
                margin=ft.margin.only(bottom=20)
            ),
            ft.Container(
                content=imagenPrin,
                alignment=ft.alignment.center,
                expand=True
            ),
            ft.Container(
                content=boton_iniciar,
                alignment=ft.alignment.bottom_center,
                margin=ft.margin.only(top=20)
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        expand=True  # Ocupa todo el espacio disponible
    )

    page.add(
        ft.Container(
            content=contenido,
            expand=True,
            alignment=ft.alignment.center
        )
    )

ft.app(main, view=ft.WEB_BROWSER, host="0.0.0.0")