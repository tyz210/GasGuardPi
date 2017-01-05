from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '240')

Builder.load_file('res/ui/gas_guard.kv')


class MainView(BoxLayout):
    pass


class GasGuardApp(App):

    def build(self):
        Window.clearcolor = (0.1176, 0.0392, 0.1176, 1)
        self.title = 'GasGuard'
        return MainView()


if __name__ == '__main__':
    app = GasGuardApp()
    app.run()
