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
                if fields[1] == "fantastically":
                    self.save_data('fantastically', fields[0])
                    #search_count=search_count+1

        #self.save_data('fantastic', search_count)

        if key is not None:
            return search_count


if __name__ == "__main__":
    reducer = LengthReducer()
    reducer.reduce(None)
