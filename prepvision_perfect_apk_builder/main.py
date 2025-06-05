from kivy.app import App
from kivy.uix.label import Label

class PrepVisionApp(App):
    def build(self):
        return Label(text="PrepVision AI Ready!")

if __name__ == '__main__':
    PrepVisionApp().run()
