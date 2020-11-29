# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 13 Exercise 4. Celsius to Fahrenheit
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import tkinter


class TempConverterGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter a temperature:')
        self.default_entry = tkinter.Entry(self.top_frame,
                                           width=26)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.default_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.default_label = tkinter.Label(self.mid_frame,
                                           text='Convert to Celsius/Fahrenheit:')

        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.response_label = tkinter.Label(self.mid_frame,
                                            textvariable=self.value)

        # Pack the middle frame's widgets.
        self.default_label.pack(side='left')
        self.response_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.cel_button = tkinter.Button(self.bottom_frame,
                                         text='Celsius',
                                         command=self.convert_celsius)
        self.fah_button = tkinter.Button(self.bottom_frame,
                                         text='Fahrenheit',
                                         command=self.convert_fahrenheit)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.cel_button.pack(side='left')
        self.fah_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.

    def convert_fahrenheit(self):
        # Get the value entered by the user into the
        #  widget.
        temperature = float(self.default_entry.get())

        # Convert Celsius to Fahrenheit.
        fahrenheit = ((9 / 5) * temperature) + 32

        # Convert fahrenheit to a string and store it
        # in the StringVar object. This will automatically
        # update the widget.
        self.value.set(f'{fahrenheit:,.1f} Fahrenheit.')

    def convert_celsius(self):
        temperature = float(self.default_entry.get())
        celsius = (temperature - 32) * (5 / 9)
        self.value.set(f'{celsius:,.1f} Celsius.')


# Create an instance of the TempConverterGUI class.
if __name__ == '__main__':
    temp_conv = TempConverterGUI()
