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
            if (len(fields)==2):
                count = int(fields[0])
                word = fields[1].lower()
                if word != current_word:
                    self.save_data(current_word, word_count)
                    if key is not None and key == current_word:
                        search_count = word_count
                    current_word = word
                    word_count = count
                else:
                    word_count = word_count + count

        # Don't forget the last page.
        self.save_data(word, word_count)
        if key is not None:
            return search_count


if __name__ == "__main__":
    reducer = LengthReducer()
    reducer.reduce(None)
