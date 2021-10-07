from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
import kivy
kivy.require("2.0.0")  # replace with your installed kivy version


class HelloWorldUI(RelativeLayout):
    # This class is required by kivy design language files
    # You can use Widget or Layout types for this class
    pass


class HelloWorld(App):
    # This class constructs the app window
    def build(self):
        # Set a custom window title
        self.title = "Hello World App"
        return HelloWorldUI()

    # callback function for button on_press event
    def button_callback(self):
        self.root.ids.greeting.text = "Hello " + self.root.ids.user.text + "!"


if __name__ == '__main__':
    # Run the GUI window
    HelloWorld().run()
