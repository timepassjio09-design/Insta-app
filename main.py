
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class InstaApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text='Insta Manager', font_size='24sp'))
        self.username = TextInput(hint_text='Username', size_hint_y=None, height=50)
        self.target = TextInput(hint_text='Jisko follow karna hai', size_hint_y=None, height=50)
        self.add_widget(self.username)
        self.add_widget(self.target)
        btn = Button(text='FOLLOW KARO', background_color=(0,1,0,1), size_hint_y=None, height=60)
        btn.bind(on_press=self.follow)
        self.add_widget(btn)
        self.status = Label(text='Status: Ready')
        self.add_widget(self.status)
    def follow(self, instance):
        self.status.text = f"{self.target.text} ko Follow kar diya!"

class MyApp(App):
    def build(self):
        return InstaApp()

MyApp().run()
