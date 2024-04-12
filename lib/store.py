from datetime import datetime, timedelta, time

from lib.opening import Opening

class Store:
    __openings: list[Opening]

    def __init__(self, opening: list[Opening] = []):
        self.__openings = opening

    @property
    def openings(self):
        return self.__openings

    def IsOpenOn(self, date: datetime):
        for opening in self.__openings:
            if opening.IsOpenOn(date):
                return True
        return False

    def NextOpeningDate(self, date: datetime):
        if self.IsOpenOn(date):
            date = self.__jump_to_non_opening_hour(date)
        while not self.IsOpenOn(date):
            date += timedelta(minutes=1)
        date = date.replace(second=0, microsecond=0)
        return date
    
    def __jump_to_non_opening_hour(self, date: datetime):
        while self.IsOpenOn(date):
            date += timedelta(minutes=1)
        return date