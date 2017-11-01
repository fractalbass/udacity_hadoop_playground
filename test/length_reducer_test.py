from length_reducer import LengthReducer as Reducer
import unittest
import mock


class ApacheLogMapperTest(unittest.TestCase):

    def test_mapper_can_parse_from_standard_in(self):
        reducer = Reducer()
        reducer.sysin = open('../data/reducer_fixture','r')
        reducer.reduce(None)

    @mock.patch('sys.stdout')
    def test_mapper_can_save_data(self, my_mock):
        reducer = Reducer()
        reducer.sysin = open('../data/reducer_fixture', 'r')
        reducer.sysout = my_mock
        reducer.reduce(None)
        self.assertTrue(my_mock.write.called, "Failed to output data message.")

    def test_reducer_counts_right(self):
        reducer = Reducer()
        reducer.sysin = open('../data/reducer_fixture', 'r')
        count = reducer.reduce('miles')
        self.assertTrue(count == 6)


