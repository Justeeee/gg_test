from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

# Define screens
class WelcomeScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class DashboardScreen(MDScreen):
    pass

class ChallengesScreen(MDScreen):
    pass

class VendorsScreen(MDScreen):
    pass

class EventsScreen(MDScreen):
    pass

class ProfileScreen(MDScreen):
    pass

class GoGreenApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("gg_ui.kv")

if __name__ == "__main__":
    GoGreenApp().run()
