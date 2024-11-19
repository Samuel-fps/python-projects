import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime
import os

Builder.load_file("design.kv")

# Pages
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "Sign_up_screen"

    def login(self, username, password):
        users = {}
        if os.path.exists("users.json"):
            try:
                with open("users.json", "r") as file:
                    users = json.load(file)
            except json.JSONDecodeError:
                print("El archivo JSON está vacío o tiene un formato incorrecto.")

        if username in users and users[username]['password'] == password:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'down'
        self.manager.current = "login_screen"

    def get_saying(self):
        if os.path.exists("saying.txt"):
            with open("saying.txt") as file:
                sayings = file.readlines()
            if sayings:
                self.ids.saying.text = random.choice(sayings).strip()
            else:
                self.ids.saying.text = "No sayings found."
        else:
            self.ids.saying.text = "Saying file not found."

class SignUpScreen(Screen):
    def add_user(self, username, password):
        users = {}
        if os.path.exists("users.json"):
            try:
                with open("users.json", "r") as file:
                    users = json.load(file)
            except json.JSONDecodeError:
                print("El archivo JSON está vacío o tiene un formato incorrecto.")
        
        users[username] = {
            'username': username, 
            'password': password,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("users.json", 'w') as file:
            json.dump(users, file)
        
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'down'
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()
