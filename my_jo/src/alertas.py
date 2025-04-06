import flet as ft

def configurar_snackbar(page: ft.Page):
    snack = ft.SnackBar(content=ft.Text(""), open=False)
    page.snack_bar = snack

    def mostrar_snack(mensaje):
        snack.content = ft.Text(mensaje)
        snack.open = True
        page.update()

    return mostrar_snack, snack
