import flet as ft

from flet import Row, Column, Icons, Colors, Container, Text, border, BoxShadow, ShadowBlurStyle, BoxShape, MainAxisAlignment, TextAlign

class StatsDisplay(Container):
    def __init__(self):
        super().__init__()
        self.changes_done      = Text("0", style=ft.TextStyle(size=15), width=75, text_align=TextAlign.RIGHT)
        self.selected_elements = Text("0", style=ft.TextStyle(size=15), width=75, text_align=TextAlign.RIGHT)
        self.stat_col = StatsColumn(self.changes_done, self.selected_elements)
        self.content = self.stat_col
        self.bgcolor = Colors.PRIMARY_CONTAINER
        self.border = border.all(1, Colors.PRIMARY_CONTAINER)
        self.border_radius = 10
        self.padding = 5
        self.shadow = BoxShadow(blur_radius=1, spread_radius=0, blur_style=ShadowBlurStyle.OUTER, color=Colors.INVERSE_SURFACE)

class StatsColumn(Column):
    def __init__(self, changes_done, selected_elements):
        super().__init__()
        self.changes_row = Row([
            Text("Total Changes:", style=ft.TextStyle(size=15), width=140),
            changes_done,
        ],
        alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        self.selected_row = Row([
            Text("Selected Elements:", style=ft.TextStyle(size=15), width=140),
            selected_elements,
        ],
        alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        self.controls = [
            self.changes_row,
            self.selected_row,
        ]