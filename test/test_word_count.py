import unittest
import mock

from length_mapper import LengthMapper


class test_word_count(unittest.TestCase):

    test_phrase = """\t\t\t\tthis is a fantastic and not very long set of words that is fantastic and organized. Very fantastic fantastic.\tblah"""

    def test_count_words(self):
        wc = LengthMapper()
        counts = wc.map(self.test_phrase)
        self.assertTrue(counts[-1][0] == 'fantastic')
        self.assertTrue(counts[-1][1] == 4)

    @mock.patch('sys.stdout')
    def test_mapper_can_parse_from_standard_in(self, my_mock):
        mapper = LengthMapper()
        mapper.sysin = open('../data/forum_500.tsv', 'r')
        mapper.sysout = my_mock
        mapper.map()
        self.assertTrue(my_mock.write.called, "Failed to call the writer!")


    def test_splitter(self):
        mapper = LengthMapper()
        txt = mapper.splitter('This is some <funky>! <p>fantastic</p>bad text')
        self.assertTrue(txt[0]=='this')
        self.assertTrue(txt[1] == 'is')
        self.assertTrue(txt[2] == 'some')
        self.assertTrue(txt[3] == 'funky')
        self.assertTrue(txt[4] == 'p')
        self.assertTrue(txt[5] == 'fantastic')
        self.assertTrue(txt[6] == 'p')
        self.assertTrue(txt[7] == 'bad')
        self.assertTrue(txt[8] == 'text')
        self.assertTrue("<" not in txt)
        self.assertTrue("T" not in txt)
