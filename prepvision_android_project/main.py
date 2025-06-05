from kivy.app import App
from kivy.uix.label import Label

class PrepVisionApp(App):
    def build(self):
        return Label(text="Hello from PrepVision AI!")

if __name__ == '__main__':
    PrepVisionApp().run()
