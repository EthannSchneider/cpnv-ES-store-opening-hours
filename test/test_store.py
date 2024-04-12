from datetime import datetime, time
import unittest

from lib.opening import Opening
from lib.store import Store
from lib.weekday import Weekdays

class TestStore(unittest.TestCase):
    store: Store

    # test dates 
    wednesday = '2024-02-21T07:45:00.000'
    thursday = '2024-02-22T12:22:11.824'
    saturday = '2024-02-24T09:15:00.000'
    sunday = '2024-02-25T09:15:00.000'
    friday_morning = '2024-02-23T08:00:00.000'
    monday_morning = '2024-02-26T08:00:00.000'
    thursday_afternoon = '2024-02-22T14:00:00.000'

    def setUp(self):
        opening = [
            Opening([Weekdays.MON, Weekdays.WED, Weekdays.FRI], time(8, 0), time(16, 0)),
            Opening([Weekdays.TUE, Weekdays.THU, Weekdays.SAT], time(8, 0), time(12, 0)),
            Opening([Weekdays.TUE, Weekdays.THU], time(14, 0), time(18, 0))
        ]
        self.store = Store(opening)

    def test_IsOpenOn(self):
        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.wednesday)), False)
        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.thursday)), False)
        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.sunday)), False)

        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.friday_morning)), True)
        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.monday_morning)), True)
        self.assertEqual(self.store.IsOpenOn(datetime.fromisoformat(self.thursday_afternoon)), True)

    def test_NextOpeningDate(self):
        self.assertEqual(self.store.NextOpeningDate(datetime.fromisoformat(self.thursday_afternoon)), datetime.fromisoformat(self.friday_morning))
        self.assertEqual(self.store.NextOpeningDate(datetime.fromisoformat(self.saturday)), datetime.fromisoformat(self.monday_morning))
        self.assertEqual(self.store.NextOpeningDate(datetime.fromisoformat(self.thursday)), datetime.fromisoformat(self.thursday_afternoon))