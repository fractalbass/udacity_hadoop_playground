import unittest
import mock

from student_times_mapper import StudentTimeMapper as Mapper
from student_times_reducer import StudentTimeReducer as Reducer


class StudentTimesTest(unittest.TestCase):

    def test_get_student_time(self):
        mapper = Mapper()
        student_time = mapper.get_student_time('"5339"	"Whether pdf of Unit and Homework is available?"	"cs101 pdf"	"100000458"	""	"question"	"\N"	"\N"	"2012-02-25 08:09:06.787181+00"	"1"	""	"\N"	"100000921"	"2012-02-25 08:11:01.623548+00""6922"	"\N"	"\N"	"204"	"f"')
        print("Student time is: {0}".format(student_time))
        self.assertTrue(student_time=='08')

    def test_get_student_id(self):
        mapper = Mapper()
        student_id = mapper.get_student_id('"5339"	"Whether pdf of Unit and Homework is available?"	"cs101 pdf"	"100000458"	""	"question"	"\N"	"\N"	"2012-02-25 08:09:06.787181+00"	"1"	""	"\N"	"100000921"	"2012-02-25 08:11:01.623548+00""6922"	"\N"	"\N"	"204"	"f"')
        print("Student id is: {0}".format(student_id))
        self.assertTrue(student_id=="5339")

    def test_get_highest_hour(self):
        reducer = Reducer()
        reducer.sysin = file.open("../data/student_times_reducer_fixture.txt")
        self.assertTrue(reducer.reduce())

    def test_get_max_hour(self):
        reducer = Reducer()
        self.assertTrue(reducer.get_max_hour([1, 1, 2, 2, 2, 3, 3]) == 2)
        self.assertTrue(reducer.get_max_hour([1, 1, 1, 1, 2, 3, 3]) == 1)
        self.assertTrue(reducer.get_max_hour([1, 2, 3, 3, 3, 3, 3]) == 3)


