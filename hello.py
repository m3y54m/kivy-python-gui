from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
import kivy
kivy.require("2.0.0")  # replace with your installed kivy version


# Class name becomes defaut window title
class HelloWorld(App):
    def build(self):
        # Set a custom windows title
        self.title = "Hello World App"
        # Create a new GridLayout for placement of windows components
        self.window = GridLayout()
        # Set number of columns in GridLayout
        self.window.cols = 1
        # GridLayout styling
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        ### Add widgets to window (GridLayout) ###

        # Display image
        self.window.add_widget(Image(source="parrot.jpg"))

        # Display text
        self.greeting = Label(
            text='Hello world!',
            # Label styling
            font_size=18,
            color="#00FFCE"
        )
        # Add Label to the GridLayout
        self.window.add_widget(self.greeting)

        # Input text
        self.user = TextInput(
            multiline=False,
            # TextInput styling
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        # Add TextInput to the GridLayout
        self.window.add_widget(self.user)

        # Add button
        self.button = Button(
            text="Say Hello!",
            # Button styling
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE",
            background_normal=""
        )
        # Bind the callback function to the button
        self.button.bind(on_press=self.button_callback)
        # Add Button to the GridLayout
        self.window.add_widget(self.button)

        return self.window

    def button_callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"


if __name__ == '__main__':
    # Run the GUI
    HelloWorld().run()
