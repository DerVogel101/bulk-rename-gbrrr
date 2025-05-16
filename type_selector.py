import flet as ft

from flet import Checkbox, Column

class TypeSelector(Checkbox):
    def __init__(self, label, handler):
        super().__init__()
        self.label = label
        self.value = False
        self.on_change = handler
        self.label_style = ft.TextStyle(size=15)

class TypeSettings(Column):
    def __init__(self):
        super().__init__()
        self.hidden_box = TypeSelector("Rename hidden Files", self.hidden_clicked)
        self.folder_box = TypeSelector("Rename Folders", self.folders_clicked)
        self.controls = [self.hidden_box, self.folder_box]

    def folders_clicked(self, event):
        ...

    def hidden_clicked(self, event):
        ...