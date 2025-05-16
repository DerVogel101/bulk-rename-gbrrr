import flet as ft

from flet import Row, Column, Icons, Colors, ElevatedButton, FilePicker, FilePickerResultEvent, ButtonStyle, TextStyle, BoxShadow, ShadowBlurStyle

class FolderSelectorButton(ElevatedButton):
    def __init__(self):
        super().__init__()
        self.icon = Icons.FOLDER_OPEN
        self.text = "Open Folder"
        self.on_click = self.open_picker
        self.file_picker = FilePicker(on_result=self.process_result)
        self.height = 50
        self.expand = True
        self.style = ButtonStyle(
            icon_size=30,
            bgcolor=Colors.PRIMARY_CONTAINER,
            shadow_color=Colors.INVERSE_SURFACE,
            text_style=TextStyle(
                size=25,
            )
        )


    def did_mount(self):
        self.page.overlay.append(self.file_picker)
        self.page.update()

    def open_picker(self, event):
        self.file_picker.get_directory_path("Select Folder")
        print(self.file_picker.result)

    def process_result(self, event: FilePickerResultEvent):
        if not event.path: return
        if len(event.path) > 40:
            self.text = "..." + event.path[-40:]
        else:
            self.text = event.path
        self.page.update()

