import flet as ft 
import time
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
    
    # Contenedor de mensajes
    chat_mensajes = ft.Column(scroll="auto", expand=True)

    # Mensaje inicial
    mensaje_inicial = (
        "Hola, ¿en qué puedo ayudarte?\n"
        "Por favor selecciona una opción escribiendo el número correspondiente:\n"
        "1. ¿Quién fundo Tunja? \n"
        "2. ¿Qué puedo hacer en Tunja?\n"
        "3. ¿Qué lugar es más visitado en Tunja?\n"
        "4. ¿Qué sitios turisticos hay en Tunja?\n"
        "5. Historia de Tunja"
    )

    # Diccionario centralizado de opciones
    #imagenes\inicial.png
    opciones = {
        "1": {
            "texto": "Tunja fue fundada por Gonzalo Suárez Rendón en 6 de agosto 1539",
            "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhy3fqLItgkrSi1lQsNbdnjhDUiQ6O_FLGgG_lwszHFRglGXn8IfY4Ke5hAKbGBjP3HL4&usqp=CAU",
            "maps": "https://maps.app.goo.gl/NKSiHmQZYBshi7pr5"
        },
        "2": {
            "texto": "Puedes visitar sitios como la casa del gobernador o sitios de comida tradicional",
            "imagen": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/9d/b1/83/casa-del-fundador-gonzalo.jpg?w=1200&h=-1&s=1",
            "maps": "https://maps.app.goo.gl/NKSiHmQZYBshi7pr5"
        },
        "3":{
            "texto": "El lugar es más visitado en Tunja es la iglesia catedralicia de Tunja, de estilo gótico y neoclásico, que es la más antigua del país (1562)",
            "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwBgyNhQuExnNi16_okRWz0kv2hmbTJjhh-w&s",
            "maps": "https://maps.app.goo.gl/Be57YXbLH5F5eJ6d7"
        }
        # Añadir más opciones aquí...
    }
    
    chat_mensajes.controls.append(
        ft.Container(
            content=ft.Text(f"Bot: {mensaje_inicial}", size=18, color="black"),
            bgcolor="#E8F5E9",  # Verde claro
            padding=10,
            border_radius=10,
            margin=5,
            alignment=ft.alignment.center_left
        )
    )


    # Campo de entrada del usuario
    entrada_usuario = ft.TextField(
        label="Escribe tu mensaje",
        expand=True
    )
    # Función que procesa los mensajes
    def procesar_mensaje(mensaje):
        return opciones.get(mensaje, {}).get("texto", "Opción inválida")
       

          
    
    def respuesta_con_imagen(mensaje):
        datos = opciones.get(mensaje, {})
        if not datos:
            return None
        componentes = []
        
      # Imagen clickeable con GestureDetector
        if "imagen" in datos and "maps" in datos:
            componentes.append(
                ft.GestureDetector(
                    content=ft.Image(
                        src=datos["imagen"],
                        width=200,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    on_tap=lambda e, url=datos["maps"]: e.page.launch_url(url)
                )
            )
        
        return ft.Column(controls=componentes) if componentes else None
          

   # Función para mostrar la respuesta del bot de manera progresiva
    def mostrar_respuesta_progresiva(respuesta):
        respuesta_parcial = ""
        for letra in respuesta:
            respuesta_parcial += letra
            # Actualizar el último mensaje (contenedor) del bot
            ultimo = chat_mensajes.controls[-1]
            if isinstance(ultimo, ft.Container) and isinstance(ultimo.content, ft.Text):
                ultimo.content.value = f"Bot: {respuesta_parcial}"
            page.update()
            chat_mensajes.scroll_to(offset=-1, duration=0)  # Mueve scroll
            time.sleep(0.02)
          
    #Fun para manejar los mensajes
    def enviar_mensaje(evento):
        # Obtener el texto ingresado
        mensaje = entrada_usuario.value.strip()
        if mensaje:
            # Mensaje del usuario
            chat_mensajes.controls.append(
                ft.Container(
                    content=ft.Text(f"Tú: {mensaje}", size=18),
                    bgcolor="#F0F0F0",
                    padding=10,
                    border_radius=10,
                    margin=5,
                    alignment=ft.alignment.center_right
                )
            )
            
            entrada_usuario.value = ""
            
            # Indicador de escritura
            escribiendo = ft.Text("Bot está escribiendo...", italic=True, color="gray")
            chat_mensajes.controls.append(escribiendo)
            page.update()
            
            time.sleep(1)
            chat_mensajes.controls.remove(escribiendo)
            
            # Obtener y mostrar respuesta
            respuesta = procesar_mensaje(mensaje)
            mostrar_respuesta_progresiva(respuesta)
            
            # Componentes adicionales
            respuesta_visual = respuesta_con_imagen(mensaje)
            if respuesta_visual:
                chat_mensajes.controls.append(
                    ft.Container(
                        content=respuesta_visual,
                        bgcolor="#E8F5E9",
                        padding=10,
                        border_radius=10,
                        margin=5,
                        alignment=ft.alignment.center_left
                    )
                )
            
            page.update()
            chat_mensajes.scroll_to(offset=-1, duration=500)

            if respuesta == "Opción inválida":
                chat_mensajes.controls.append(
                    ft.Container(
                        content=ft.Text(f"Bot: {mensaje_inicial}", size=18, color="black"),
                        bgcolor="#E8F5E9",
                        padding=10,
                        border_radius=10,
                        margin=5,
                        alignment=ft.alignment.center_left
                    )
                )
                page.update()
                chat_mensajes.scroll_to(offset=-1, duration=500)


     # Botón de enviar
    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensaje)




    return ft.View(
        "/hTunja",
        appbar=appbar,
        drawer=page.drawer, 
        controls=[
            ft.Container(
                content=chat_mensajes,
                expand=True,
                padding=20
            ),
            ft.Row(  
                controls=[entrada_usuario, boton_enviar],
                spacing=10,
                alignment="center"
            )
        ]
    )
