from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

Builder.load_file("design.kv")

# Pages
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "Sign_up_screen"

class SignUpScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()