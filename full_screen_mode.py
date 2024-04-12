import tkinter as tk

from lib.opening import Opening
from lib.store import Store

class FullScreenMode(tk.Tk):
    def __init__(self, openings : list[Opening]):
        super().__init__()

        self.store = Store(openings)

        self.title('Store Opening Hours')
        self.geometry('300x50')
        self.attributes('-fullscreen', True)

        self.label = tk.Label(self, text="Store Opening Hours", font=("Arial", 56))
        self.label.pack()

        for opening in self.store.openings:
            text: str = ""
            for day in opening.day:
                text += f"{day.name}, "
            
            text += f"\b\b from {opening.open.strftime('%H:%M')} to {opening.close.strftime('%H:%M')}"
            
            self.label = tk.Label(self, text=text, font=("Arial", 48), anchor='w')
            self.label.pack()
