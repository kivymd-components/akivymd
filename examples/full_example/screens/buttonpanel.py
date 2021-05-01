from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string(
    """
<ButtonPanel@AKButtonPanel>:
    pos:60,150
    icon:'plus'
    selectable:True

    MDIconButton:
        icon:'minus'
        theme_text_color: "Custom"
        text_color:1,1,0,1

    MDIconButton:
        icon:'calendar'
        theme_text_color: "Custom"
        text_color:1,0,0,1

    MDIconButton:
        icon:'android'
        theme_text_color: "Custom"
        text_color:0,1,1,1
    """

)

class ButtonPanel(MDScreen):
    pass
