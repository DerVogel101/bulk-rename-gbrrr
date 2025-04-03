import flet as ft

from flet import Row, Column, Icons, Colors

class BasePage(Column):
    def __init__(self):
        super().__init__()
        self.scroll = True
        self.alignment = ft.MainAxisAlignment.START
        self.controls = [
            HeaderRow(),
        ]

class HeaderRow(Row):
    def __init__(self):
        super().__init__()
        self.controls = [
                    ft.Text("Bulk Rename Gbrrr"),
                    ft.IconButton(
                        icon=ft.icons.CLOSE,
                        icon_color=ft.colors.RED_400,
                        tooltip="Close",
                        on_click=lambda e: self.page.window.close(),
                    ),
                ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN