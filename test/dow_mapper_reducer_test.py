from dow_mapper import DOWMapper as Mapper
from dow_reducer import DOWReducer as Reducer
import unittest
import mock


class DOWMapperTest(unittest.TestCase):

    def test_parse_date_amt(self):
        dm = Mapper()
        weekday, amt = dm.parse_date_amt("2012-02-07	09:44	Santa Ana	Children's Clothing	110.38	Cash")
        self.assertTrue(weekday == "Tuesday")
        self.assertTrue(amt == 110.38)

    def test_reducer(self):
        reducer = Reducer()
        reducer.sysin = open('../data/dow_reducer_fixture.txt','r')
        x = reducer.reduce("Sunday")
        self.assertTrue(x == 61.0)