
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicStringsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Strings"
        self.root = Builder.load_file('dynamic_strings.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)

DynamicStringsApp().run()
