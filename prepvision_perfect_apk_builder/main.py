from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Welcome label
        self.welcome_label = Label(
            text="PrepVision AI Ready!",
            font_size='24sp',
            size_hint_y=0.3
        )
        self.add_widget(self.welcome_label)

        # Start button
        self.start_button = Button(
            text="Start Analysis",
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.5}
        )
        self.start_button.bind(on_press=self.on_start_pressed)
        self.add_widget(self.start_button)

    def on_start_pressed(self, instance):
        self.welcome_label.text = "Analysis Starting..."

class PrepVisionApp(App):
    def build(self):
        # Set background color
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return MainScreen()

if __name__ == '__main__':
    PrepVisionApp().run()