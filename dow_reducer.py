#!/usr/bin/python
import sys
import math

class DOWReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def get_average(self, l):
        total = 0
        for x in l:
            total = total + x
        return total/len(l)

    # Note:  This calculates the POPULATION stdev.  The sample stdev is
    # done differently.
    def get_stdev(self, l):
        total = 0.0
        for x in l:
            total = total + long(x)
        a = long(total/len(l))
        v = 0.0
        for x in l:
            v = v + math.pow((a - long(x)),2)

        stdev = math.sqrt(v/len(l))
        return stdev


    def reduce(self, q):
        result = None
        current_day = None
        day_sales = list()
        count_days = 0
        for line in self.sysin:
            fields = line.split()
            if len(fields) == 2:
                if current_day is None:
                    current_day = fields[0]

                if fields[0] != current_day:
                    #Done with this day.  Summarize and print
                    ave = self.get_average(day_sales)
                    self.save_data(current_day, ave)
                    if current_day == q:
                        result = ave
                    day_sales = [long(fields[1])]
                    current_day = fields[0]

                else:
                    day_sales.append(long(fields[1]))

        ave = self.get_average(day_sales)
        self.save_data(current_day, ave)
        if current_day == q:
            result = ave
        return result

if __name__ == "__main__":
    reducer = DOWReducer()
    reducer.reduce("Sunday")
