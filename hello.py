import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# Class name becomes window title
class HelloWorld(App):
    def build(self):
        # Create a new GridLayout
        self.window = GridLayout()
        # Set number of columns
        self.window.cols = 1

        #Add widgets to window
        self.window.add_widget(Image(source="parrot.jpg"))

        self.greeting = Label(text='Hello world!')
        self.window.add_widget(self.greeting)

        return self.window


if __name__ == '__main__':
    # Run the GUI
    HelloWorld().run()