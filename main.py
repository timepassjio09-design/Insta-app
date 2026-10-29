from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class InstaManagerApp(App):
    def build(self):
        self.ids_list = []
        self.groups = {}
        self.master_id = None
        self.auto_post = False
        self.auto_follow = False
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        root.add_widget(Label(text='Insta Manager - Master Control', font_size=20, size_hint_y=0.1))
        
        # Add ID
        b1 = BoxLayout(size_hint_y=0.1)
        self.id_input = TextInput(hint_text='Enter ID')
        btn1 = Button(text='Add ID', size_hint_x=0.3)
        btn1.bind(on_press=self.add_id)
        b1.add_widget(self.id_input); b1.add_widget(btn1)
        root.add_widget(b1)
        
        # Group
        b2 = BoxLayout(size_hint_y=0.1)
        self.group_input = TextInput(hint_text='Group Name')
        btn2 = Button(text='Create Group', size_hint_x=0.4)
        btn2.bind(on_press=self.create_group)
        b2.add_widget(self.group_input); b2.add_widget(btn2)
        root.add_widget(b2)
        
        # Master
        b3 = BoxLayout(size_hint_y=0.1)
        b3.add_widget(Label(text='Master:'))
        self.spinner = Spinner(text='Select Master', values=[])
        self.spinner.bind(text=self.set_master)
        b3.add_widget(self.spinner)
        root.add_widget(b3)
        
        # Switches
        g = GridLayout(cols=2, size_hint_y=0.2)
        g.add_widget(Label(text='Auto Post ON/OFF')); self.s1 = Switch(); self.s1.bind(active=self.set_post); g.add_widget(self.s1)
        g.add_widget(Label(text='Auto Follow ON/OFF')); self.s2 = Switch(); self.s2.bind(active=self.set_follow); g.add_widget(self.s2)
        root.add_widget(g)
        
        self.lbl = Label(text='IDs: 0\\nMaster: None\\nAuto Post OFF\\nAuto Follow OFF')
        sv = ScrollView(); sv.add_widget(self.lbl); root.add_widget(sv)
        
        b4 = BoxLayout(size_hint_y=0.1)
        b4.add_widget(Button(text='Post with Master', on_press=self.do_post))
        b4.add_widget(Button(text='Follow with Master', on_press=self.do_follow))
        root.add_widget(b4)
        return root
    
    def add_id(self, _): 
        v=self.id_input.text.strip()
        if v and v not in self.ids_list: self.ids_list.append(v); self.id_input.text=''; self.refresh()
    def create_group(self, _):
        v=self.group_input.text.strip()
        if v: self.groups[v]=self.ids_list.copy(); self.group_input.text=''; self.refresh()
    def set_master(self, sp, txt): self.master_id=txt; self.refresh()
    def set_post(self, _, val): self.auto_post=val; self.refresh()
    def set_follow(self, _, val): self.auto_follow=val; self.refresh()
    def refresh(self):
        self.spinner.values=self.ids_list
        self.lbl.text=f"IDs: {len(self.ids_list)} {self.ids_list}\\nMaster: {self.master_id}\\nGroups: {list(self.groups.keys())}\\nAuto Post: {'ON - sab me jayegi' if self.auto_post else 'OFF - sirf master me'}\\nAuto Follow: {'ON - sab follow' if self.auto_follow else 'OFF - sirf master'}"
    def do_post(self, _): self.lbl.text=f"{self.master_id} se post -> {'All IDs' if self.auto_post else 'Only Master'} me gayi"
    def do_follow(self, _): self.lbl.text=f"{self.master_id} ne follow kiya -> {'All IDs' if self.auto_follow else 'Only Master'} ne follow kiya"

InstaManagerApp().run()
