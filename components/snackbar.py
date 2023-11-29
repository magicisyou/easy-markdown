import flet as ft

from utils import variables as var

def show_snackbar(message):
    var.PAGE.snack_bar = ft.SnackBar(
        content=ft.Row(
            controls=[
                ft.Text(message, color=ft.colors.ON_SURFACE_VARIANT),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.SURFACE_VARIANT,
        show_close_icon=True,
    )
    var.PAGE.snack_bar.open = True
    var.PAGE.update()