#!/usr/bin/python
import sys


class LengthReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def reduce(self, key):
        word = ""
        current_word = None
        word_count = 0
        search_count = 0

        for line in self.sysin:
            fields = line.split()
            if len(fields) == 2:
                self.save_data(fields[0], fields[1])

        if key is not None:
            return search_count


if __name__ == "__main__":
    reducer = LengthReducer()
    reducer.reduce(None)
