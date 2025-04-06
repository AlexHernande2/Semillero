import flet as ft
import threading
import time
from nn.chbot import chatBOT

def contInicial(page: ft.Page):
    # Borra el contenido actual de la página
    page.views.clear()
    page.title = "Sitios_de_Interes"
    titulo = ft.Text("HOLA PAGINA Ndd", size=30)
    
     # Función para navegar a la segunda página
    def ir_a_pagina_chat(evento):
        chatBOT(page)  # Llama a la función para cargar la segunda página
     # Botón
    boton_chat = ft.ElevatedButton(
        "Chat",
        on_click=ir_a_pagina_chat,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=10)
        ),
    )
     
    titulo = ft.Text("Sitios de Interes",
                     size=30,
                     text_align=ft.TextAlign.CENTER             
    )
    
    # Lista de imágenes
    imagenes = [
        "https://cdn.pixabay.com/photo/2015/10/01/17/17/car-967387_960_720.png",
        "https://cdn.pixabay.com/photo/2017/09/01/00/15/png-2702691_1280.png",
        "https://cdn.pixabay.com/photo/2017/02/04/22/37/panther-2038656_960_720.png"
    ]

    # Definir el índice actual usando ft.Ref()
    indice_actual = ft.Ref()
    indice_actual.current = 0

    # Imagen principal
    imagen_mostrada = ft.Image(
        src=imagenes[indice_actual.current],  # Usar .current en lugar de .value
        fit="contain",
        width=300,
        height=300
    )
    
    # Función para cambiar de imagen
    def cambiar_imagen(direccion):
        if direccion == "anterior":
            indice_actual.current = (indice_actual.current - 1) % len(imagenes)
        elif direccion == "siguiente":
            indice_actual.current = (indice_actual.current + 1) % len(imagenes)
        elif direccion == "auto":
            indice_actual.current = (indice_actual.current + 1) % len(imagenes)
        imagen_mostrada.src = imagenes[indice_actual.current]
        page.update()
    #Funcion para cambiar la imagen por tiempo
    def cambio_automatico():
        while True:
            time.sleep(5)  # cada 5 segundos
            cambiar_imagen("auto")
    
    # Inicia el temporizador en un hilo separado
    threading.Thread(target=cambio_automatico, daemon=True).start()
    
    # GestureDetector para detectar gestos táctiles
    gesture_detector = ft.GestureDetector(
            content=imagen_mostrada,
        on_horizontal_drag_update=lambda e: cambiar_imagen(
            "anterior" if e.primary_delta > 0 else "siguiente"  
        ),
    )   
    
    page.views.append(
        ft.View(
           # "/inicio",  # Ruta de esta página
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content= ft.Column(
                                [
                                    ft.Container(
                                    content=titulo,
                                    alignment=ft.alignment.center,
                                    padding=ft.padding.only(top=20, bottom=50),
                                    ),
                                    gesture_detector,  # Imagen táctil 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                        ),
                        ft.Container(
                            content=boton_chat,
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=100)  
                        ),
                    ],
                )
            ],
        )
    )
    
    page.update()