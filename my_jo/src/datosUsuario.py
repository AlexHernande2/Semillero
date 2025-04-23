import flet as ft
from user_data import usuario_existe
from appBar import MiAppBar
from alertas import configurar_snackbar #  POO


def datosUsuario(page: ft.Page):
    
    page.title = "IngresoUsuario"
    # titulo = ft.Text(
    #     "Iniciar Sesion", size=30
    # )
    appbar = MiAppBar(page, titulo="Iniciar Sesion", bgcolor="#7AE2CF",actions=[]).obtener()

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
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER, #Muestra el teclado númerico
        input_filter= ft.InputFilter(allow=True, regex_string=r"\d*") #para solo numeros
                                
    )
    boton_verificar = ft.ElevatedButton("Ingresar", on_click=verificar)

    logoSesión = ft.Image(
        src="https://static.vecteezy.com/system/resources/previews/024/553/630/non_2x/colorful-owl-pop-art-style-owl-sticker-pastel-cute-colors-ai-generated-png.png",
        fit="contain",
        width=300
        )
    
    return ft.View(
        "/datos_usuario",
        appbar=appbar,
        controls=[
            ft.Container(
                width=350,
                height=400,
                padding=20,
                border_radius=10,
                bgcolor= ft.colors.SURFACE_VARIANT,
                alignment= ft.alignment.center,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                logoSesión
                            ]
                        ),
                     
                        ft.Row(
                            controls=[
                                campo_cedula
                            ]
                        ),
                        ft.Row(
                            controls=[
                                boton_verificar
                            ]
                        ),

                    ], expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER
                )
            )
            # ft.Column(
            #     [
            #         titulo,
            #         campo_cedula,
            #         boton_verificar,
            #         snack  
            #     ],
            #     alignment=ft.MainAxisAlignment.CENTER,
            #     horizontal_alignment=ft.CrossAxisAlignment.CENTER
            # )
        ]
    )
