from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MyMobileApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Add the centered label
        label = Label(text="Enter Your Text:", halign='center', font_size=20)
        layout.add_widget(label)

        # Add the text input field
        text_input = TextInput(multiline=False)
        layout.add_widget(text_input)

        # Create and add individual buttons (modify button text and functionality as needed)
        button1 = Button(text="Button 1", on_press=self.button_clicked)
        layout.add_widget(button1)

        button2 = Button(text="Button 2", on_press=self.button_clicked)
        layout.add_widget(button2)

        button3 = Button(text="Button 3", on_press=self.button_clicked)
        layout.add_widget(button3)

        button4 = Button(text="Button 4", on_press=self.button_clicked)
        layout.add_widget(button4)

        button5 = Button(text="Button 5", on_press=self.button_clicked)
        layout.add_widget(button5)

        button6 = Button(text="Button 6", on_press=self.button_clicked)
        layout.add_widget(button6)

        button7 = Button(text="Button 7", on_press=self.button_clicked)
        layout.add_widget(button7)

        button8 = Button(text="Button 8", on_press=self.button_clicked)
        layout.add_widget(button8)

        button9 = Button(text="Button 9", on_press=self.button_clicked)
        layout.add_widget(button9)

        return layout

    def button_clicked(self, instance):
        # Handle button press events (e.g., print button text, access text input value)
        text = f"Button '{instance.text}' (Button 1) clicked!"
        self.show_popup(text)  # Call the generic message box function

    def show_popup(self, message):
        # Create and display the message box
        popup = Popup(title='Message', content=Label(text=message),
                      auto_dismiss=True)  # Closes automatically
        popup.open()

if __name__ == '__main__':
    MyMobileApp().run()
