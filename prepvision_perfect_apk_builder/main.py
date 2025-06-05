from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20, 40]  # Horizontal, Vertical padding
        self.spacing = 20

        # App title
        self.title_label = Label(
            text="PrepVision AI",
            font_size='32sp',
            bold=True,
            color=get_color_from_hex('#2196F3'),
            size_hint_y=0.2
        )
        self.add_widget(self.title_label)

        # Welcome message
        self.welcome_label = Label(
            text="Welcome to PrepVision AI\nYour intelligent study companion",
            font_size='18sp',
            halign='center',
            size_hint_y=0.3,
            color=get_color_from_hex('#424242')
        )
        self.add_widget(self.welcome_label)

        # Start Analysis button with better styling
        self.start_button = Button(
            text="Start Analysis",
            size_hint=(None, None),
            size=(250, 70),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#2196F3'),
            background_normal='',
            font_size='20sp'
        )
        self.start_button.bind(on_press=self.on_start_pressed)
        self.add_widget(self.start_button)

        # Status label
        self.status_label = Label(
            text="Ready to analyze",
            font_size='16sp',
            size_hint_y=0.2,
            color=get_color_from_hex('#757575')
        )
        self.add_widget(self.status_label)

    def on_start_pressed(self, instance):
        # Animate the button press
        anim = Animation(size=(240, 65), duration=0.1) + Animation(size=(250, 70), duration=0.1)
        anim.start(self.start_button)
        
        # Update status
        self.status_label.text = "Analysis in progress..."
        self.status_label.color = get_color_from_hex('#2196F3')

class PrepVisionApp(App):
    def build(self):
        # Set window background color to a light material design color
        Window.clearcolor = get_color_from_hex('#FAFAFA')
        return MainScreen()

if __name__ == '__main__':
    PrepVisionApp().run()