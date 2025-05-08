import flet as ft
import threading
import time
from appBar import MiAppBar
from chbot import chatBOT

def contInicial(page: ft.Page):
   
    page.title = "Sitios_de_Interes"
   
    mi_appbar = MiAppBar (
        page, 
        titulo= "Tunja",
        bgcolor="#CC2B52",      
        titulo_size=28,                              # tamaño de fuente
        titulo_weight=ft.FontWeight.BOLD,               #negrilla
        mostrar_volver=True, 
        mostrar_menu=True

    )
    appbar= mi_appbar.obtener()

    def abrir_maps(e):
        sitio_actual = sitios_tunja[indice_actual.current]  # Acceder al índice actual
        page.launch_url(sitio_actual["maps_url"])  # Usar la URL correspondiente


    # # Lista de imágenes
    sitios_tunja = [
        {
            "nombre": "Plaza de Bolívar",
            "imagen": "https://lh3.googleusercontent.com/gps-cs-s/AB5caB_XIjsJAcD_DfNlIkEuAs9Rl1N80XCiMcDBA1_KDMjVSuC5Er9X22yZ7W3_VsidGhmXI8KqnY2kWm18U2s0OGI7tIEBUYDZPhg-hxRaHtDNBsl9lj-DaqWhEvVdEywL2bZfCUclKQ=s1360-w1360-h1020",
            "maps_url": "https://maps.app.goo.gl/tAwZwxxZnrQiQhGa7"
        },
        {
            "nombre": "Puente de Boyacá",
            "imagen": "https://media.cnn.com/api/v1/images/stellar/prod/cnne-1243888-colombia-independence-boyaca-anniversary.jpg?q=w_1110,c_fill",
            "maps_url": "https://maps.app.goo.gl/GF12wJp3pgXAfBQj9"
        },
        {
            "nombre": "Delicias Boyacenses",
            "imagen": "https://mercadobecampo.com/cdn/shop/products/arepaboyacense.jpg?v=1626360383",
            "maps_url": "https://maps.app.goo.gl/VEV5zWnaus24Z758A"
        },
        {
            "nombre": "Centro Comercial Viva",
            "imagen": "https://ccviva.com/sites/default/files/2024-08/tunja-fachada.jpg",
            "mapa_url": "https://maps.app.goo.gl/q3Qn9Two65DmbdW38"
        },
        {
            "nombre": "Paredón de los Mártires",
            "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/JAVIER107.jpg/500px-JAVIER107.jpg",
            "mapa_url": "https://maps.app.goo.gl/hLrkA2rfbEVjS6at7"
        }
    ]
    # Lógica del carrusel
    indice_actual = ft.Ref[int]()  # Usar Ref tipado
    indice_actual.current = 0

   # Imagen principal
    imagen_mostrada = ft.Image(
        src=sitios_tunja[indice_actual.current]["imagen"],  # Usar .current en lugar de .value
        width=300,
        height=300,
        fit=ft.ImageFit.COVER  # Ajuste de imagen
    )

   # 2) Detector de tap sólo sobre la imagen
    imagen_con_tap = ft.GestureDetector(
        on_tap=abrir_maps,
        content=imagen_mostrada
    )


    titulo_sitio = ft.Text(
        value=sitios_tunja[indice_actual.current]["nombre"],
        size=20,
        weight=ft.FontWeight.BOLD
    )

    def actualizar_ui():
        imagen_mostrada.src = sitios_tunja[indice_actual.current]["imagen"]
        titulo_sitio.value = sitios_tunja[indice_actual.current]["nombre"]
        page.update()

    def cambiar_imagen(direccion: str):
        if direccion == "anterior":
            indice_actual.current = (indice_actual.current - 1) % len(sitios_tunja)
        else:
            indice_actual.current = (indice_actual.current + 1) % len(sitios_tunja)
        actualizar_ui()

    # Navegación automática
    def cambio_automatico():
        while True:
            time.sleep(5)
            cambiar_imagen("siguiente")

    threading.Thread(target=cambio_automatico, daemon=True).start()


    # Controles de navegación
    botones = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: cambiar_imagen("anterior"),
            ),
            ft.IconButton(
                icon=ft.Icons.ARROW_FORWARD,
                on_click=lambda e: cambiar_imagen("siguiente"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Gestos táctiles
    def on_horizontal_drag(e: ft.DragUpdateEvent):
        if abs(e.delta_x) > 10:  # Sensibilidad del gesto
            cambiar_imagen("anterior" if e.delta_x > 0 else "siguiente")


    def irchat(evento):
        page = evento.page
        if page.session.contains_key("cedula"):
            page.go("/chatbot")
        else:
            # Mostrar error si no hay usuario logueado
            page.snack_bar = ft.SnackBar(ft.Text("Primero debes iniciar sesión"))
            page.snack_bar.open = True
            page.update()

    boton_chat = ft.FloatingActionButton(
        icon=ft.Icons.FORUM_OUTLINED,  # Ícono de chat
        bgcolor="#4CAF50",  # Color verde estilo WhatsApp
        shape=ft.CircleBorder(),
        width=60,
        height=60,
        mini=True,
        tooltip="Chat de asistencia",
        on_click=irchat
        # on_click=lambda e: chatBOT(page) 
    )

    def ir_Hist_Tunja (e):
        page.go("/hTunja")
        print("hola")   

    btn_H_Tj = ft.Container(
        margin=ft.margin.only(top=20),
        content=ft.ElevatedButton(
            "Historia de Tunja",
            
            bgcolor="#CC2B52",      # color de fondo
            color="white",          # color del texto
            width=200,              # ancho fijo en píxeles
            height=50,             # (opcional) alto fijo
            on_click= ir_Hist_Tunja

        )
    )    
    


    gestos = ft.GestureDetector(
        on_horizontal_drag_update=on_horizontal_drag,
        content=ft.Column(
            controls=[
                # imagen_mostrada,
                imagen_con_tap,
                titulo_sitio,
                botones,
                boton_chat,
                btn_H_Tj
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    return ft.View(
        "/inicio",
        appbar=appbar,
        drawer=page.drawer,
        controls=[
            ft.Container(
                content=gestos,
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )

   
