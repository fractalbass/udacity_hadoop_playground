#!/usr/bin/python
import logging
import sys
from datetime import datetime

sys.path.append('./')

class DOWMapper():

    logging.basicConfig(filename='mapper.log')
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sysin = sys.stdin
    sysout = sys.stdout

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def parse_date_amt(self, line):
        amt = None
        weekday = None
        try :
            fields = line.split('\t')
            weekday = datetime.strptime(fields[0], "%Y-%m-%d").weekday()
            amt = fields[4]
        except Exception as ex:
            logging.WARN("Error {0} raw data: {1}".format(ex.message, line))
        return self.days[weekday], float(amt)

    def map(self):

        for line in self.sysin:
            amt, weekday  = self.parse_date_amt(line)
            self.save_data(amt, weekday)

#Do the work
if __name__ == "__main__":
    mapper = DOWMapper()
    mapper.map()