import flet as ft
from user_data import guardar_usuario
from alertas import configurar_snackbar
from appBar import MiAppBar

def formulario_usuario(page, ced ):
    print("Entró a formulario_usuario con cédula:", ced)

    page.title = "Registro de Usuario"
   
    appbar = MiAppBar(
        page, titulo="REGISTRO USUARIO",
        bgcolor="#CC2B52",
        actions=[],        
        titulo_size=28,                              # tamaño de fuente
        titulo_weight=ft.FontWeight.BOLD,               #negrilla
        mostrar_volver=True 
    ).obtener()

    #Se utiliza POO puesw con el fin de no repetir código
    mostrar_snack, snack = configurar_snackbar(page)

   #Diccionario de sub-categorías
    opciones_sub = {
        "Comida": ["Restaurantes", "Cafés", "Street Food"],
        "Deporte": ["Fútbol", "Baloncesto", "Natación"],
        "Cultura y Arte": ["Museos", "Galerías", "Teatro"],
        "Entretenimiento": ["Cine", "Conciertos", "Parques de diversiones"]
    }

    #Campos para la recolección de datos
    cedula = ft.Text(f"Cédula: {ced}",expand=True, size=16)
    edad = ft.TextField(label="Edad", expand=True)
    sexo = ft.Dropdown(
        label="Sexo",
        options=[ft.dropdown.Option("M"), ft.dropdown.Option("F")],
        expand=True,
        width=float("inf")
    )
    
    tiempoDisponible = ft.TextField(
        label="Tiempo disponible en horas",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Entre 1 y 8",
        expand=True,
        width=float("inf")
    )

    intereses = ft.Dropdown(
        label="intereses", options=
            [
                ft.dropdown.Option(k) 
                for k in opciones_sub.keys()
            ],
            expand=True,
            width=float("inf")
        )
    
    subInteres = ft.Dropdown(
        label="SubInteres", 
        options=[],
        expand=True,
        width=float("inf")
    )

    def on_interes_cambiado(e):
        sel = e.control.value
        # Obtener las opciones apropiadas
        lista = opciones_sub.get(sel, [])
        # Reconstruir opciones de subInteres
        subInteres.options = [ft.dropdown.Option(op) for op in lista]
        subInteres.value = None        # limpiar selección previa
        subInteres.update()            # refrescar componente

    intereses.on_change = on_interes_cambiado

     # Configurar snackbar
    mostrar_snack, snack = configurar_snackbar(page)
    def guardar(evento):

        if not all([
            edad.value, sexo.value, intereses.value, subInteres.value,
            tiempoDisponible.value
        ]):
            mostrar_snack("Debe ingresar todos los campos")
            return

        try:
            edad_int = int(edad.value)
            if not 18 <= edad_int <= 70:
                mostrar_snack("Edad fuera de rango. Debes tener entre 18 y 70 años.")
                return
        except ValueError:
            mostrar_snack("Edad inválida. Ingresa un número.")
            return

        try:
            tiempo_int = int(tiempoDisponible.value)
            if not 1 <= tiempo_int <= 8:
                mostrar_snack("Tiempo disponible fuera de rango. Debe ser entre 1 y 8 horas.")
                return
        except ValueError:
            mostrar_snack("Tiempo disponible inválido. Ingresa un número.")
            return

        data = {
            "Edad": edad_int,
            "Sexo": sexo.value,
            "Tiempo disponible": tiempo_int,
            "Interes": intereses.value,
            "subInteres": subInteres.value,
            
        }

        guardar_usuario(ced, data)
        page.go("/inicio")  
     

    boton_guardar = ft.ElevatedButton(
        "Guardar",
        on_click=guardar,
        bgcolor="#CC2B52",      # color de fondo
        color="white",          # color del texto
        width=200,              # ancho fijo en píxeles
        height=50               # (opcional) alto fijo
    )    
    

    conPrincipal = ft.Container(
        expand=True,
        padding=20,
        border_radius=10,
        gradient= ft.LinearGradient(
            rotation=0.5,
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
             colors=[
                "#c8b4f0",  # lila claro
                "#f0c8f0",  # rosa pastel
                "#c8f0ff",  # celeste pastel
            ]
        ),
        content=ft.Column(
            controls=[
                cedula,
                edad,
               ft.Container(  # Envuelve el Dropdown de sexo en un Container
                    content=sexo,
                    expand=True  # Fuerza al Container a expandirse
                ),
                ft.Container(
                    content=tiempoDisponible,
                    expand=True
                ),
                ft.Container(
                    content=intereses,
                    expand=True
                ),
                ft.Container(
                    content=subInteres,
                    expand=True
                ),
                boton_guardar,
                snack
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
           
        )

    )

    return ft.View(
        f"/formulario_usuario?ced={ced}",
        appbar=appbar,
        controls=[
            ft.Container(
                content= conPrincipal,
                # expand=True
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente en la View
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


