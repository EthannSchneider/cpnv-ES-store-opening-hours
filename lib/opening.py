from datetime import datetime, time
from lib.weekday import Weekdays

class Opening:
    day : list[Weekdays]
    open : time
    close : time

    def __init__(self, day: list[Weekdays], open: time, close: time):
        if len(day) == 0:
            raise ValueError("At least one day must be specified")
        if open >= close:
            raise ValueError("Open time must be before close time")
        self.day = day
        self.open = open
        self.close = close

    def IsOpenOn(self, date: datetime):
        for day in self.day:
            if date.weekday() == day.value:
                return self.open <= date.time() and date.time() <= self.close
        return False
