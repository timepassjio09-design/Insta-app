from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.storage.jsonstore import JsonStore

store = JsonStore('ids.json')

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        self.add_widget(Label(text='INSTA-APP : ID Group Manager', size_hint_y=None, height=50, bold=True, font_size=22))
        
        # Add ID
        add_box = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.id_input = TextInput(hint_text='New ID likho jaise Raja123')
        add_btn = Button(text='Add ID', size_hint_x=0.3)
        add_btn.bind(on_press=self.add_id)
        add_box.add_widget(self.id_input)
        add_box.add_widget(add_btn)
        self.add_widget(add_box)
        
        # Master ID
        master_box = BoxLayout(size_hint_y=None, height=40, spacing=5)
        master_box.add_widget(Label(text='Master ID:'))
        self.master_label = Label(text='Koi ID nahi', bold=True)
        master_box.add_widget(self.master_label)
        self.add_widget(master_box)
        
        # Switches - Tera wala feature
        switch_box1 = BoxLayout(size_hint_y=None, height=40)
        switch_box1.add_widget(Label(text='Auto Post: 1 ID se = Sab pe'))
        self.auto_post_switch = Switch(active=True)
        switch_box1.add_widget(self.auto_post_switch)
        self.add_widget(switch_box1)
        
        switch_box2 = BoxLayout(size_hint_y=None, height=40)
        switch_box2.add_widget(Label(text='Auto Follow: 1 se = Sab se'))
        self.auto_follow_switch = Switch(active=True)
        switch_box2.add_widget(self.auto_follow_switch)
        self.add_widget(switch_box2)
        
        # Group
        group_box = BoxLayout(size_hint_y=None, height=40, spacing=5)
        self.group_input = TextInput(hint_text='Group Name jaise Mera Group')
        group_btn = Button(text='Create Group', size_hint_x=0.3)
        group_btn.bind(on_press=self.create_group)
        group_box.add_widget(self.group_input)
        group_box.add_widget(group_btn)
        self.add_widget(group_box)
        
        # IDs List
        self.add_widget(Label(text='Tumhari IDs:', size_hint_y=None, height=30))
        self.scroll = ScrollView()
        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        self.scroll.add_widget(self.list_layout)
        self.add_widget(self.scroll)
        
        # Post
        post_box = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.post_input = TextInput(hint_text='Master se kya post karna hai?')
        post_btn = Button(text='POST', size_hint_x=0.3, background_color=(0,0.6,1,1))
        post_btn.bind(on_press=self.make_post)
        post_box.add_widget(self.post_input)
        post_box.add_widget(post_btn)
        self.add_widget(post_box)
        
        self.status = Label(text='Status: Ready - Kitni bhi ID add kar sakte ho', size_hint_y=None, height=30)
        self.add_widget(self.status)
        self.refresh_list()
    
    def add_id(self, instance):
        new_id = self.id_input.text.strip()
        if not new_id: return
        ids = store.get('data')['ids'] if store.exists('data') else []
        if new_id not in ids:
            ids.append(new_id)
            master = store.get('data').get('master', ids[0]) if store.exists('data') else ids[0]
            store.put('data', ids=ids, master=master)
        self.id_input.text = ''
        self.refresh_list()
    
    def create_group(self, instance):
        gname = self.group_input.text.strip()
        if gname:
            store.put('group', name=gname)
            self.status.text = f'Group Created: {gname}'
            self.group_input.text = ''
    
    def set_master(self, id_name):
        data = store.get('data')
        store.put('data', ids=data['ids'], master=id_name)
        self.refresh_list()
    
    def refresh_list(self):
        self.list_layout.clear_widgets()
        if not store.exists('data'): return
        data = store.get('data')
        ids = data.get('ids', [])
        master = data.get('master', ids[0] if ids else '')
        self.master_label.text = master
        for i in ids:
            row = BoxLayout(size_hint_y=None, height=45, spacing=5)
            is_master = ' [MASTER]' if i==master else ''
            row.add_widget(Label(text=f'{i}{is_master}', size_hint_x=0.6))
            btn = Button(text='Master Banao', size_hint_x=0.4)
            btn.bind(on_press=lambda x, id_name=i: self.set_master(id_name))
            row.add_widget(btn)
            self.list_layout.add_widget(row)
    
    def make_post(self, instance):
        text = self.post_input.text.strip()
        if not text or not store.exists('data'): return
        data = store.get('data')
        ids = data.get('ids', [])
        master = data.get('master', ids[0])
        if self.auto_post_switch.active:
            self.status.text = f'POSTED by {master} -> {len(ids)} IDs pe gaya!'
        else:
            self.status.text = f'POSTED only by {master}'
        self.post_input.text = ''

class InstaApp(App):
    def build(self):
        return MainLayout()

InstaApp().run()
