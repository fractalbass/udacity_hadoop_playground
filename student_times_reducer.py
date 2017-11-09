#!/usr/bin/python
import sys
import logging


class StudentTimeReducer():
    sysin = sys.stdin
    sysout = sys.stdout

    logging.basicConfig(filename='student_time_reducer.log')

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}".format(key, value))

    def get_max_hour(self, l):
        return max(l, key=l.count)

    def reduce(self, studentId):
        student = None
        previous_student = None
        student_hours = list()
        for l in self.sysin:
            try:
                student, hour = l.split('\t')

                if previous_student is None:
                    previous_student = student

                if student != previous_student:
                    self.save_data(previous_student, self.get_max_hour(student_hours))
                    student_hours=list()
                    student_hours.append(hour)
                    previous_student = student
                else:
                    student_hours.append(hour)

            except Exception as ex:
                logging.error("Error processing line: {0}".format(l))

        self.save_data(student, self.get_max_hour(student_hours))


        return None

if __name__ == '__main__':
    reducer = StudentTimeReducer()
    reducer.reduce(None)