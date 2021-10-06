import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class HelloWorld(App):

    def build(self):

        self.greeting = Label(text='Hello world!')
        
        return self.greeting


if __name__ == '__main__':
    HelloWorld().run()