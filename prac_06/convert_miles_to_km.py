from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_convert(self):
        result = self.get_valid_input() * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        result = self.get_valid_input() + increment
        self.root.ids.input_value.text = str(result)

    def get_valid_input(self):
        try:
            value = float(self.root.ids.input_value.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKm().run()
