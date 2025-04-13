import flet as ft
import threading
import time
# from nn.chbot import chatBOT

def contInicial(page: ft.Page):
    # Borra el contenido actual de la página
    page.views.clear()
    page.title = "Sitios_de_Interes"
    titulo = ft.Text("HOLA PAGINA Ndd", size=30)
    
     # Función para navegar a la segunda página
    # def ir_a_pagina_chat(evento):
    #     chatBOT(page)  # Llama a la función para cargar la segunda página
     # Botón
    boton_chat = ft.ElevatedButton(
        "Chat",
        #on_click=ir_a_pagina_chat,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=10)
        ),
    )
     
    titulo = ft.Text("Sitios de Interes",
                     size=30,
                     text_align=ft.TextAlign.CENTER             
    )
    
    # Lista de imágenes
    sitios_tunja = [
        {
            "nombre": "Plaza de Bolívar",
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AB5caB_XIjsJAcD_DfNlIkEuAs9Rl1N80XCiMcDBA1_KDMjVSuC5Er9X22yZ7W3_VsidGhmXI8KqnY2kWm18U2s0OGI7tIEBUYDZPhg-hxRaHtDNBsl9lj-DaqWhEvVdEywL2bZfCUclKQ=s1360-w1360-h1020",
            "maps_url": "https://maps.app.goo.gl/tAwZwxxZnrQiQhGa7"
        },
        {
            "nombre": "Puente de Boyacá",
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AB5caB-kBx9RQOOB1Au7ITurj0pBla4eJ3u5MY36272jZXT2s_sStJmo_EzK692hAfOhlx9XWCHikzVrxaJTy2JevXxeaR7805c68jlaewwpUbADsa7pWUNTWBIB3nfrQE80acy3ILBt=w243-h174-n-k-no-nu",
            "maps_url": "https://maps.app.goo.gl/GF12wJp3pgXAfBQj9"
        },
        {
            "nombre": "Catedral Basílica Metropolitana Santiago de Tunja",
            "imagen": "https://lh3.googleusercontent.com/p/AF1QipOUU0qZPR-YJUrWZFV_P9qRgKc-7JxhA9VKlD6Y=w408-h544-k-no",
            "maps_url": "https://maps.app.goo.gl/WDr6vQfc1q23KZwu7"
        }
    ]

    def abrir_maps(e):
        sitio = sitios_tunja[indice_actual.current]
        page.launch_url(sitio["maps_url"])



    # Definir el índice actual usando ft.Ref()
    indice_actual = ft.Ref()
    indice_actual.current = 0

    # Imagen principal
    imagen_mostrada = ft.Image(
        src=sitios_tunja[indice_actual.current]["imagen"],  # Usar .current en lugar de .value
        fit="contain",
        width=300,
        height=300
    )
    
    # Función para cambiar de imagen
    def cambiar_imagen(direccion):
        if direccion == "anterior":
            indice_actual.current = (indice_actual.current - 1) % len(sitios_tunja)
        elif direccion == "siguiente":
            indice_actual.current = (indice_actual.current + 1) % len(sitios_tunja)
        elif direccion == "auto":
            indice_actual.current = (indice_actual.current + 1) % len(sitios_tunja)
        imagen_mostrada.src = sitios_tunja[indice_actual.current]["imagen"]
        imagen_mostrada.update()
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
        on_tap=abrir_maps
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