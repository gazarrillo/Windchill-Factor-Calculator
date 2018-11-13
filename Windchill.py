from tkinter import *

class WindchillGUI:
    def __init__(self):

        self.title_frame = Frame()
        self.top_frame = Frame()
        self.mid_frame = Frame()
        self.mid_frame2 = Frame()
        self.bottom_frame = Frame()

        self.tile_label = Label(self.title_frame, font = ('none', 20), text = 'Windchill Factor Calculator')
        self.prompt_label1 = Label(self.top_frame, text = 'Enter the temperature in Fareheit')
        self.prompt_label2 = Label(self.mid_frame, text = 'Enter the wind speed in mph')
        self.temp_entry = Entry(self.top_frame, width = 10)
        self.speed_entry = Entry(self.mid_frame, width = 10)

        self.tile_label.pack(side = 'top')
        self.prompt_label1.pack(side = 'left')
        self.prompt_label2.pack(side = 'left')
        self.temp_entry.pack(side = 'left')
        self.speed_entry.pack(side = 'left')

        self.calc_button = Button(self.bottom_frame, text='Calculate Windchill', command = self.windchillFactor)
        self.calc_button.pack(side='left')

        self.descr_label = Label(self.mid_frame2, text='The windchill temperature is: ')

        self.value = StringVar()
        self.output_label = Label(self.mid_frame2, textvariable = self.value)

        self.descr_label.pack(side='left')
        self.output_label.pack(side='left')

        self.title_frame.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.mid_frame2.pack()

    def windchillFactor(self):
        """This function calculates the windchill factor"""
        temperature = float(self.temp_entry.get())
        speed = float(self.speed_entry.get())
        windchill = 35.74 + 0.6215 * temperature - 35.75 * speed**0.16 + 0.4275 * temperature * speed**0.16
        self.value.set(round(windchill, 1))

root = Tk()
root.title('Windchill Calculator')
WindchillGUI()
root.mainloop()
