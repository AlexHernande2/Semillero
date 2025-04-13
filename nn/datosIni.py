import flet as ft
import datetime
from my_jo.src.inicio import contInicial


def datosUsuario(page: ft.Page):
    #limpiar la pantalla
    page.views.clear()
    page.title = "Datos"
    
    titulo= ft.Text(
        "Registro",
        size=30,
        text_align=ft.TextAlign.CENTER
 
    ) 
    
    def irpaginaIni(evento):
        contInicial (page)
        
        
    txt_name = ft.TextField(label="Nombre") 
    txt_lastname = ft.TextField(label="Apellido") 
    
     # Obtener la fecha actual
    fecha_actual = datetime.datetime.today().strftime("%d-%m-%Y")
    # Campo de fecha (prellenado con la fecha actual)
    # read_only=True evita que el usuario ingrese manualmente la fecha para que lo haga solo con DatePicker
    txt_fecha = ft.TextField(label="Fecha de nacimiento", value=fecha_actual, read_only=True)
    
     # Función para el cambio de fecha
    def handle_change(e):
        if date_picker.value:
            txt_fecha.value = date_picker.value.strftime("%d-%m-%Y")  # Actualiza con la fecha elegida
            page.update()

    # Crear el DatePicker con fecha actual preseleccionada
    date_picker = ft.DatePicker(
        first_date=datetime.datetime(year=1950, month=1, day=1),  # Rango para las fechas
        last_date=datetime.datetime(year=2009, month=12, day=31),
        value=datetime.datetime.today(),  # Fecha actual seleccionada por defecto
        on_change=handle_change,  # Se ejecuta cuando el usuario elige una fecha
    )

    # Agregar DatePicker al overlay
    page.overlay.append(date_picker)
    
      # Botón para abrir el selector de fecha
    btn_fecha = ft.ElevatedButton(
        " Seleccionar fecha de nacimiento",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda e: date_picker.pick_date(),  # Abre el selector
    )
    
    btn_Siguiente = ft.ElevatedButton(
        "Siguiente", 
        on_click= irpaginaIni
    )
    
    contenido = ft.Container(
        content=titulo,
        alignment=ft.alignment.center
    )
   
    
    contenidoCuerpo = ft.Column(
        controls=[txt_name,txt_lastname,txt_fecha, btn_fecha, btn_Siguiente]
    )
    
    page.views.append(
       ft.View(
            route="/registro",
            controls=[contenido, contenidoCuerpo]
        )
    )
    
    page.update()
    