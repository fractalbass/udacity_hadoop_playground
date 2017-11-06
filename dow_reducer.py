#!/usr/bin/python
import sys
import numpy as np

class DOWReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def reduce(self, q):
        result = None
        current_day = None
        day_sales = list()
        for line in self.sysin:
            fields = line.split()
            if len(fields) == 2:
                if current_day is None:
                    current_day = fields[0]

                if fields[0] != current_day:
                    #Done with this day.  Summarize and print
                    ave = np.average(day_sales, axis=0)
                    self.save_data(current_day, ave)
                    if current_day == q:
                        result = ave
                    day_sales = [float(fields[1])]
                    current_day = fields[0]

                else:
                    day_sales.append(float(fields[1]))

        ave = np.average(day_sales, axis=0)
        self.save_data(current_day, ave)
        if current_day == q:
            result = ave
        return result

if __name__ == "__main__":
    reducer = DOWReducer()
    reducer.reduce("Sunday")
