from kivy.app import App
from kivy.lang import Builder
# from kivy.app import StringProperty

M_TO_KM = 1.609

class ConvertMilesKm(App):
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_miles()
        result = value * M_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_up_down(self, change):
        value = self.get_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertMilesKm().run()