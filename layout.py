import flet as ft

from flet import Row, Column, Icons, Colors, IconButton
from flet.core.types import MainAxisAlignment

from file_picker import FolderSelectorButton
from type_selector import TypeSettings
from stats_display import StatsDisplay
from item_lists import ElementListContainer

class BasePage(Column):
    def __init__(self):
        super().__init__()
        self.scroll = True
        self.alignment = ft.MainAxisAlignment.START
        self.controls = [
            HeaderRow(),
            FileListRow()
        ]

class ThemeChanger(IconButton):
    def __init__(self):
        super().__init__()
        self.icon = Icons.WB_SUNNY_OUTLINED
        self.icon_color = Colors.RED_400
        self.tooltip = "Change Theme"
        self.on_click = self.theme_change

    def theme_change(self, event):
        self.page.theme_mode = ft.ThemeMode.LIGHT if self.page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.page.update()

class HeaderRow(Row):
    def __init__(self):
        super().__init__()
        self.controls = [
            FolderSelectorButton(),
            TypeSettings(),
            StatsDisplay(),
            ThemeChanger(),
        ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

class FileListRow(Row):
    def __init__(self):
        super().__init__()
        self.controls = [
            ElementListContainer(),
            ElementListContainer(),
        ]
        self.alignment = MainAxisAlignment.SPACE_AROUND
