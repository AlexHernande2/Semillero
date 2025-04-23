import flet as ft
from user_data import usuario_existe
from appBar import MiAppBar
from alertas import configurar_snackbar #  POO


def datosUsuario(page: ft.Page):
    
    page.title = "IngresoUsuario"

    appbar = MiAppBar(page, titulo="Iniciar Sesion", actions=[]).obtener()

    #POO
    mostrar_snack, snack = configurar_snackbar(page)

    def verificar(evento):
        ced = campo_cedula.value.strip()
        if not ced:
           mostrar_snack("Ingresa una cédula válida")
           return

        if not ced.isdigit():
            mostrar_snack("Deben ser solo números")
            return
        
        numero_cedula = int(ced)
        if numero_cedula < 22_300_000 or numero_cedula > 2_000_000_000:
            mostrar_snack("Los rangos permitidos son de 22_300_000 y de 2_000_000_000")
            return
        
        page.session.set("cedula", ced)

        if usuario_existe(ced):
            page.go("/inicio")
            print("hola")
        else:
            page.go(f"/formulario_usuario?ced={ced}")

    campo_cedula = ft.TextField(     
        label="Ingresa tu cédula", 
        expand=True, #Para que se adapte al tamaño de la pantalla
        keyboard_type=ft.KeyboardType.NUMBER, #Muestra el teclado númerico
        input_filter= ft.InputFilter(allow=True, regex_string=r"\d*") #para solo numeros
                                
    )
    boton_verificar = ft.ElevatedButton(
          "Ingresar",
          on_click=verificar,
          bgcolor="#CC2B52",      # color de fondo
          color="white",          # color del texto
          width=200,              # ancho fijo en píxeles
          height=50               # (opcional) alto fijo
        
    )

    logoSesion = ft.Image(
        src="https://static.vecteezy.com/system/resources/previews/024/553/630/non_2x/colorful-owl-pop-art-style-owl-sticker-pastel-cute-colors-ai-generated-png.png",
        fit="contain",
        expand=True
        )
    
    conPrincipal = ft.Container(
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
        width=400,
        content=ft.Column(
            controls=[
                logoSesion,
                campo_cedula,
                boton_verificar,
                snack,
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            # Centramos cada hijo en el eje X
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    return ft.View(
        "/datos_usuario",
        appbar=appbar,
        controls=[
             ft.Container(
                content=conPrincipal,
                # expand=True,                      # ocupa todo el alto disponible
                alignment=ft.alignment.center,     # centra vertical y horizontal
                padding=ft.padding.all(20)
            )

        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente en la View
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente en la View
    )
