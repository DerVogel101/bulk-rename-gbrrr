import flet as ft

from flet import Row, Column, Margin, Padding, VerticalDivider, Icons, BorderSide, Colors, Container, Text, border, BoxShadow, ShadowBlurStyle, BoxShape, MainAxisAlignment, TextAlign, ListView, TextStyle

class ElementList(ListView):
    def __init__(self):
        super().__init__()
        self.spacing = 10
        self.padding = 20
        #self.width = 300
        self.height = 600
        self.expand = True

class NameFileElement(Text):
    def __init__(self, text: str):
        super().__init__()
        self.value = text
        self.style = TextStyle(size=15)
        self.expand = True

class DateFileElement(Text):
    def __init__(self, text: str):
        super().__init__()
        self.value = text
        self.style = TextStyle(size=15)

class ElementRow(Row):
    def __init__(self, name: str, date: str):
        super().__init__()
        self.controls = [
            NameFileElement(name),
            Container(margin=0, border=border.only(left=BorderSide(1)), content=Text(" ", style=TextStyle(size=15))),
            DateFileElement(date)
        ]
        self.alignment = MainAxisAlignment.CENTER

class ElementListHeader(Container):
    def __init__(self):
        super().__init__()
        self.content = Row([Text("Filename", style=TextStyle(size=15), expand=True), Text("Last Modified", style=TextStyle(size=15))])
        self.border = border.only(bottom=BorderSide(1))
        self.expand = True
        self.padding = Padding(10, 0, 32, 0)
        self.margin = Margin(10, 0, 10, 0)

class ElementListContainer(Container):
    def __init__(self):
        super().__init__()
        self.elem_list = ElementList()
        self.header = ElementListHeader()
        self.content = Column(controls=[
            self.header,
            self.elem_list,
        ], expand=True)
        self.expand = True
        self.border_radius = 20
        self.border = border.all(1, Colors.PRIMARY_CONTAINER)
        self.shadow = BoxShadow(blur_radius=1, spread_radius=0, blur_style=ShadowBlurStyle.OUTER,
                                color=Colors.INVERSE_SURFACE)
        self.padding = 5
        self.bgcolor = Colors.PRIMARY_CONTAINER
        self.margin = 5

    def did_mount(self):
        for i in range(1000):
            self.elem_list.controls.append(ElementRow(f"File{i}.test", "01.01.2001 00:00"))
        self.page.update()