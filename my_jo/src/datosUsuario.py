import flet as ft
from user_data import usuario_existe
from formulario import formulario_usuario
from alertas import configurar_snackbar #  POO
from inicio import contInicial

def datosUsuario(page: ft.Page):
    page.clean()
    page.title = "IngresoUsuario"

    titulo = ft.Text(
        "Iniciar Sesiofn", size=30
    )
       # Función para navegar a la segunda página
    def ir_a_pagina_Inicio(evento):
        contInicial(page)  # Llama a la función para cargar la segunda página

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
            ir_a_pagina_Inicio(None)
            print("hola")
        else:
            formulario_usuario(page, ced)

    campo_cedula = ft.TextField(     
        label="Ingresa tu cédula", 
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER, #Muestra el teclado númerico
        input_filter= ft.InputFilter(allow=True, regex_string=r"\d*") #para solo numeros
                                
    )
    boton_verificar = ft.ElevatedButton("Ingresar", on_click=verificar)

    layout = ft.Column(
        [
            titulo,
            campo_cedula,
            boton_verificar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Agregar los controles, incluyendo el SnackBar
    page.add(layout, snack)
    page.update()
