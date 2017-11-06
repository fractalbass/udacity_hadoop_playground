#!/usr/bin/python
import sys

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

    def reduce(self, q):
        result = None
        current_day = None
        day_sales = 0
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
                    day_sales = [float(fields[1])]
                    current_day = fields[0]

                else:
                    day_sales.append(float(fields[1]))

        ave = self.get_average(day_sales, axis=0)
        self.save_data(current_day, ave)
        if current_day == q:
            result = ave
        return result

if __name__ == "__main__":
    reducer = DOWReducer()
    reducer.reduce("Sunday")
