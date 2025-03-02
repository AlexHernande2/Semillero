import flet as ft 
import time

def chatBOT(page: ft.Page):
    # Borra el contenido actual de la página
    page.views.clear()
    page.title = "ChatBot"
    
    # Título
    titulo = ft.Text("CHATBOT", size=30)
    
    # Historial del chat
    historial_chat = ft.Column(
                scroll="auto",
                expand=True,    # Ocupa el espacio disponible
                
                
        )  # Para guardar los mensajes
    
    # Mensaje inicial
    mensaje_inicial = (
        "Hola, ¿en qué puedo ayudarte?\n"
        "Por favor selecciona una opción escribiendo el número correspondiente:\n"
        "1. ¿Qué puedo hacer en Tunja?\n"
        "2. ¿Qué lugar es más visitado en Tunja?\n"
        "3. ¿Qué sitios turisticos hay en Tunja?"
    )
    # mensaje inicial 
    historial_chat.controls.append(ft.Text(f"Bot: {mensaje_inicial}", size=18, color="blue"))
    
    # Campo de entrada del usuario
    entrada_usuario = ft.TextField(
        label="Escribe tu mensaje",
        width=300,
    )

    # Función para manejar los mensajes del usuario
    def enviar_mensaje(evento):
        # Obtener el texto ingresado
        mensaje = entrada_usuario.value.strip()
        
        if mensaje:
            # Agregar el mensaje del usuario 
            historial_chat.controls.append(ft.Text(f"Tú: {mensaje}", size=18))
           
            # Limpiar el campo de entrada
            entrada_usuario.value = ""
            
            mensajeBot_escribiendo = ft.Text("Bot está escribiendo...", size=16, italic=True, color="gray")
            
            historial_chat.controls.append(mensajeBot_escribiendo)
            page.update()
            
            #retraso para responder 
            time.sleep(1)
            
            # Respuesta del chatbot
            respuesta = procesar_mensaje(mensaje)
            
            # Eliminar el  "Bot está escribiendo..."
            historial_chat.controls.remove(mensajeBot_escribiendo)
            
            
            # Mostrar la respuesta del bot de manera progresiva
            mostrar_respuesta_progresiva(respuesta)
            
            
             # Desplazar el scroll al final
            historial_chat.scroll_to(offset=-1, duration=500)  # Desplaza al final
            page.update()
             #Mostrar imagenes 
            if mensaje== "1":
                imagenes()
            
    # Función para mostrar la respuesta del bot de manera progresiva
    def mostrar_respuesta_progresiva(respuesta):
        respuesta_parcial = ""
        for letra in respuesta:
            respuesta_parcial += letra
            # Actualizar el último mensaje del bot
            if len(historial_chat.controls) > 0 and isinstance(historial_chat.controls[-1], ft.Text):
                historial_chat.controls[-1].value = f"Bot: {respuesta_parcial}"
            else:
                historial_chat.controls.append(ft.Text(f"Bot: {respuesta_parcial}", size=18, color="blue"))
            page.update()
            time.sleep(0.05)  # Retraso entre cada letra
    
    def imagenes():
            # Título de la imagen
        titulo_catedral = ft.Text("Catedral Basílica Metropolitana de Tunja", size=16, weight=ft.FontWeight.BOLD)
        
        # Imagen de la Catedral de Tunja
        imagen_catedral = ft.Image(
            src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/23/23/c5/catedral-basilica-metropolitan.jpg?w=800&h=-1&s=1", 
            width=200,
            height=150,
            fit=ft.ImageFit.CONTAIN,
        )
        
        # Título de la segunda imagen
        titulo_puente = ft.Text("Paredón de los Mártires de Tunja", size=16, weight=ft.FontWeight.BOLD)
        
        # Imagen del Paredón de los Mártires
        imagen_puente = ft.Image(
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSegNA4Wt1wnFDZaOLhnm7XVDfSmx2hGePISA&s", 
            width=200,
            height=150,
            fit=ft.ImageFit.CONTAIN,
        )
        
        # Contenedor para las imágenes
        contenedor = ft.Column(
            controls=[
                titulo_catedral, 
                imagen_catedral,
                titulo_puente,
                imagen_puente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10  # Espacio entre los elementos
        )
        
        # Agregar el contenedor al historial del chat
        historial_chat.controls.append(contenedor)
         
        
    # Función que procesa los mensajes y genera respuestas
    def procesar_mensaje(mensaje):
      match mensaje:
          case "1":
              return "Puedes visitar:"
          case "2":
                return "El lugar más visitado en Tunja es la Plaza de Bolívar."
          case "3":
                return "aun nada"              
          case "_.":
                return "Opción invalida"
            
    
    
    # Botón de enviar
    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensaje)
    


    # Construcción de la interfaz
    page.views.append(
        ft.View(
            "/chbot",
            controls=[
                titulo,
                historial_chat,
                ft.Row(
                    [entrada_usuario, boton_enviar],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
   
    page.update()
