from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class VelocicodeMobile(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # [🇧🇪] Brand Header
        self.root.add_widget(Label(text="V", font_size='80sp', color=(0, 1, 0.8, 1)))
        self.root.add_widget(Label(text="VELOCICODE V1", font_size='24sp'))

        # Search Bar
        self.search = TextInput(hint_text='Search 1000+ Scripts...', multiline=False, size_hint_y=None, height=50)
        self.search.bind(text=self.filter_scripts)
        self.root.add_widget(self.search)

        # Scrollable Script List
        self.scroll = ScrollView()
        self.list_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        
        # Your 1000 Scripts
        self.all_scripts = [f"Script {i}" for i in range(1, 1001)]
        self.populate_list(self.all_scripts)
        
        self.scroll.add_widget(self.list_layout)
        self.root.add_widget(self.scroll)
        
        # Attach Button
        btn = Button(text="ATTACH 🇧🇪", size_hint_y=None, height=60, background_color=(0, 1, 0.8, 1))
        self.root.add_widget(btn)
        
        return self.root

    def populate_list(self, script_list):
        self.list_layout.clear_widgets()
        for s in script_list:
            btn = Button(text=s, size_hint_y=None, height=40)
            self.list_layout.add_widget(btn)

    def filter_scripts(self, instance, value):
        filtered = [s for s in self.all_scripts if value.lower() in s.lower()]
        self.populate_list(filtered)

if __name__ == '__main__':
    VelocicodeMobile().run()
