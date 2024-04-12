from datetime import time
import tkinter as tk

from full_screen_mode import FullScreenMode
from lib.opening import Opening
from lib.weekday import Weekdays

class app(tk.Tk):
    __openings : list[Opening] = []
    __title : tk.Label
    __day_list : tk.Listbox
    __day_string_list: tk.StringVar
    __opening_day_list : tk.Listbox
    __opening_day_string_list: tk.StringVar
    __opening_hours_text : tk.Label
    __opening_hours_input : tk.Entry
    __opening_minutes_text : tk.Label
    __opening_minutes_input : tk.Entry
    __closing_hours_text : tk.Label
    __closing_hours_input : tk.Entry
    __closing_minutes_text : tk.Label
    __closing_minutes_input : tk.Entry
    __submit_button : tk.Button
    __delete_button : tk.Button
    __full_screen_button : tk.Button

    def __init__(self):
        super().__init__()

        # app title / size
        self.title("Store Hours App")
        self.geometry("800x600")

        # Title
        self.__title = tk.Label(text="Store Opening Hours", font=("Arial", 24))
        self.__title.pack()

        # Days selection

        self.__day_string_list = tk.StringVar()
        self.__day_string_list.set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

        self.__day_list = tk.Listbox(self, listvariable=self.__day_string_list, selectmode="multiple")

        self.__day_list.pack()

        # Opening Hours selection

        self.__opening_hours_text = tk.Label(text="Opening Hours")
        self.__opening_hours_input = tk.Entry(validate="key", validatecommand=(self.register(lambda text: self.__hour_check(text)), "%P"))

        self.__opening_minutes_text = tk.Label(text="Opening Minutes")
        self.__opening_minutes_input = tk.Entry(validate="key", validatecommand=(self.register(lambda text: self.__minute_check(text)), "%P"))
        
        self.__opening_hours_text.pack()
        self.__opening_hours_input.pack()
        self.__opening_minutes_text.pack()
        self.__opening_minutes_input.pack()

        # Closing Hours selection

        self.__closing_hours_text = tk.Label(text="Closing Hours")
        self.__closing_hours_input = tk.Entry(validate="key", validatecommand=(self.register(lambda text: self.__hour_check(text)), "%P"))

        self.__closing_minutes_text = tk.Label(text="Closing Minutes")
        self.__closing_minutes_input = tk.Entry(validate="key", validatecommand=(self.register(lambda text: self.__minute_check(text)), "%P"))

        self.__closing_hours_text.pack()
        self.__closing_hours_input.pack()
        self.__closing_minutes_text.pack()
        self.__closing_minutes_input.pack()

        # Submit button to add to the list of openings hours

        self.__submit_button = tk.Button(text="Submit", command=self.__submit)
        self.__submit_button.pack()

        # List of openings hours entered

        self.__opening_day_string_list = tk.StringVar()
        self.__opening_day_string_list.set([])

        self.__opening_day_list = tk.Listbox(self, listvariable=self.__opening_day_string_list, selectmode="single")

        self.__opening_day_list.pack()

        self.__delete_button = tk.Button(text="Delete", command=lambda: self.__opening_day_list.delete(self.__opening_day_list.curselection()))
        self.__delete_button.pack()

        # Full screen button to enter into full screen mode to put on the viterine

        self.__full_screen_button = tk.Button(text="Full Screen", command=lambda: FullScreenMode(self.__openings).mainloop())
        self.__full_screen_button.pack()
    
    def __submit(self):
        selected_days = self.__day_list.curselection()
        open = time(hour=int(self.__opening_hours_input.get()), minute=int(self.__opening_minutes_input.get()))
        close = time(hour=int(self.__closing_hours_input.get()), minute=int(self.__closing_minutes_input.get()))
        weekdays = []
        for day in selected_days:
            weekdays.append(Weekdays(day))
        opening = Opening(weekdays, open, close)
        self.__openings.append(opening)
        self.__opening_day_list.insert(tk.END, self.__tranfrom_opening_to_string(opening))

        self.__opening_hours_input.delete(0, tk.END)
        self.__opening_minutes_input.delete(0, tk.END)
        self.__closing_hours_input.delete(0, tk.END)
        self.__closing_minutes_input.delete(0, tk.END)
        self.__day_list.selection_clear(0, tk.END)

    def __hour_check(self, text):
        if text == "" or (text.isdigit() and int(text) < 24):
            return True
        return False

    def __minute_check(self, text):
        if text == "" or (text.isdigit() and int(text) < 60):
            return True
        return False
    
    def __tranfrom_opening_to_string(self, opening: Opening):
        text: str = ""
        for day in opening.day:
            text += f"{day.name}, "
        
        text += f"\b\b from {opening.open.strftime('%H:%M')} to {opening.close.strftime('%H:%M')}"

        return text
    
app().mainloop()