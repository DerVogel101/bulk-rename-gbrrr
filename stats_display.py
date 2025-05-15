import flet as ft

from flet import Row, Column, Icons, Colors, Container, Text, border, BoxShadow, ShadowBlurStyle, BoxShape

class StatsDisplay(Container):
    def __init__(self):
        super().__init__()
        self.changes_done      = Text("Total Changes:     0", style=ft.TextStyle(size=15))
        self.selected_elements = Text("Selected Elements: 0", style=ft.TextStyle(size=15))
        self.stat_col = StatsColumn(self.changes_done, self.selected_elements)
        self.content = self.stat_col
        self.bgcolor = Colors.PRIMARY_CONTAINER
        self.border = border.all(1, Colors.PRIMARY_CONTAINER)
        self.border_radius = 10
        self.shadow = BoxShadow(blur_radius=1, spread_radius=0, blur_style=ShadowBlurStyle.OUTER, color=Colors.INVERSE_SURFACE)

class StatsColumn(Column):
    def __init__(self, changes_done, selected_elements):
        super().__init__()
        self.controls = [
            changes_done,
            selected_elements,
        ]