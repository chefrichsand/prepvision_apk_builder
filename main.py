
from kivy.app import App
from kivy.uix.button import Button
import os

class DeployApp(App):
    def build(self):
        return Button(
            text='Deploy PrepVision AI',
            font_size=24,
            on_press=self.deploy
        )

    def deploy(self, instance):
        os.system("termux-open-url https://raw.githubusercontent.com/chefrichsand/prepvision/main/prepvision_android_installer.sh")

if __name__ == '__main__':
    DeployApp().run()
