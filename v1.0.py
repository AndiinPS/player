from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MusicPlayer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        play_button = Button(text='Play Music')
        layout.add_widget(play_button)
        return layout

if __name__ == '__main__':
    MusicPlayer().run()
