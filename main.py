import flet as ft

from utils import app, variables

def main(page: ft.Page):
    page.title = "Easy Markdown"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.PURPLE_300)
    variables.update_variables(page)
    page.add(app.content())

ft.app(target=main,assets_dir="assets")
