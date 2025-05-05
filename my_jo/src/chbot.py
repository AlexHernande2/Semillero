import flet as ft
import json
from appBar import MiAppBar
from modelo import predecir_sitios  # Importar la función de predicción

def chatBOT(page: ft.Page):
    page.title = "Asistente Virtual"
    
    # AppBar personalizado
    appbar = MiAppBar(
        page, 
        titulo="Asistente Virtual",
        bgcolor="#4CAF50",
        mostrar_volver=True
    ).obtener()
    
    # Contenedor de mensajes
    chat_mensajes = ft.Column(scroll="auto", expand=True)
    
    # Función para mostrar recomendaciones
    def mostrar_recomendaciones():
        try:
            # Obtener cédula de la sesión
            cedula = page.session.get("cedula")
            
            # Cargar datos del usuario
            with open("usuarios.json") as f:
                usuarios = json.load(f)
                datos = usuarios.get(cedula, {})
            
            if not datos:
                chat_mensajes.controls.append(ft.Text("❌ Error: Usuario no registrado"))
                return
            
            # Hacer predicción
            sitios = predecir_sitios(datos)
            
            # Mostrar resultados
            recomendaciones = ft.Column([
                ft.Text("¡Tus sitios recomendados! 🎯", size=18, weight="bold"),
                ft.Text(f"1. {sitios[0]}"),
                ft.Text(f"2. {sitios[1]}"),
                ft.Text(f"3. {sitios[2]}")
            ])
            
            chat_mensajes.controls.append(
                ft.Container(
                    content=recomendaciones,
                    bgcolor="#E8F5E9",
                    padding=15,
                    border_radius=10,
                    margin=5
                )
            )
            
        except Exception as e:
            chat_mensajes.controls.append(
                ft.Text(f"⚠️ Error: {str(e)}", color="red")
            )
        
        page.update()
    
    # Mostrar recomendaciones al cargar la vista
    mostrar_recomendaciones()
    
    # Diseño de la vista
    return ft.View(
        "/chatbot",
        appbar=appbar,
        controls=[
            ft.Container(
                content=chat_mensajes,
                expand=True,
                padding=20
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START
    )