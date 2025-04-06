import flet as ft
from user_data import guardar_usuario
from alertas import configurar_snackbar

def formulario_usuario(page, ced ):
    print("Entró a formulario_usuario con cédula:", ced)

    page.clean()
    page.title = "IRegistro de Usuario"
 

    titulo = ft.Text("REGISTRO USUARIO",
                     size=30,
                     text_align=ft.TextAlign.CENTER, 
                     width=page.width              
    )
    #Se utiliza POO puesw con el fin de no repetir código
    mostrar_snack, snack = configurar_snackbar(page)


    def guardar(evento):

        if not all ([
             edad.value, sexo.value, intereses.value, nivelEstudio.value,
             tiempoDisponible.value, presupuesto.value, transporte.value
        ]):
            mostrar_snack("Debe ingresar todos los campos")
            return 

        data = {
            "edad": int(edad.value),
            "sexo": sexo.value,
            "intereses": intereses.value.split(","),
            "medio_transporte": transporte.value,
            "nivel de estudio": nivelEstudio.value,
            "tiempo disponible": tiempoDisponible.value,
            "presupuesto": presupuesto.value
        }
        guardar_usuario(ced, data)
     

    cedula = ft.Text(f"Cédula: {ced}", size=16)

    edad = ft.TextField(label="Edad")

    sexo = ft.Dropdown(label="Sexo", options=[ft.dropdown.Option("M"), ft.dropdown.Option("F")])

    intereses = ft.Dropdown(
        label="intereses", options=
            [
                ft.dropdown.Option("Plaza de Bolívar"),
                ft.dropdown.Option("Templo de Santo Domingo"), 
                ft.dropdown.Option("Pozo de Donato"),
                ft.dropdown.Option("Viva"),
                ft.dropdown.Option("Unicentro")
            ]
        )
    
    nivelEstudio = ft.Dropdown(
        label="Nivel de estudio", 
        options=[
            ft.dropdown.Option("Secundaria"),
            ft.dropdown.Option("Pregrado"),
            ft.dropdown.Option("Posgrado")
        ]
    )
    
    tiempoDisponible = ft.TextField(
        label="Tiempo disponible en horas",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Entre 1 y 15"
    )

    presupuesto= ft.Dropdown(label="Presupuesto", options=[ft.dropdown.Option("Bajo"), ft.dropdown.Option("Medio"), ft.dropdown.Option("Alto")])
    
    transporte = ft.Dropdown (
        label= "Medio de Transporte", options=
        [
            ft.dropdown.Option("A pie"), 
            ft.dropdown.Option("Vehiculo propio"), 
            ft.dropdown.Option("Transporte publico"),
            ft.dropdown.Option("Cicla")
        ]
    )

    boton_guardar = ft.ElevatedButton(
        "Guardar",
        on_click=guardar,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(horizontal=20, vertical=10)
        ),
    )    
    
    page.add(
        ft.Column(
            [
                titulo,
                cedula,
                edad,
                sexo, 
                intereses,
                nivelEstudio,
                tiempoDisponible,
                presupuesto,
                transporte,
                boton_guardar,
                snack
            ]
        )
    )

    page.update()
 

