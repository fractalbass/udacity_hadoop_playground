#!/usr/bin/python

import sys
import logging

class StudentTimeMapper():

    sysin = sys.stdin
    sysout = sys.stdout

    logging.basicConfig(filename='student_time_mapper.log')

    def get_student_time(self, line):
        return line.split('\t')[8].split(" ")[1].split(":")[0]

    def get_student_id(self, line):
        return line.split('\t')[0].replace('"',"")

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def map(self):
        linenum = 0
        for l in self.sysin:
            try:
                linenum = linenum + 1
                id = self.get_student_id(l)
                hour = self.get_student_time(l)
                self.save_data(id, hour)
            except Exception as ex:
               logging.warn("Error processing line {0}.  Skipping it.".format(linenum))


if __name__ == '__main__':
    mapper = StudentTimeMapper()
    mapper.map()
