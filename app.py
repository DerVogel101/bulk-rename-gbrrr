import flet as ft
from flet import MainAxisAlignment, CrossAxisAlignment

from layout import BasePage

def main(page: ft.Page):
    page.title = "Bulk Rename Gbrrr"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = MainAxisAlignment.START
    page.horizontal_alignment = MainAxisAlignment.CENTER

    page.add(
        BasePage()
    )

ft.app(main)