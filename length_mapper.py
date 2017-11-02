#!/usr/bin/python
import logging
import sys
import operator

sys.path.append('./')

class LengthMapper():

    logging.basicConfig(filename='mapper.log')
    word_list = list()

    sysin = sys.stdin
    sysout = sys.stdout

    specialChar = ['.', ',', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/', ' ']

    def splitter(self, words):
        words = words.lower()
        for c in self.specialChar:
            words = words.replace(c, " ")
        split = words.split(" ")

        return split

    def process(self, words):

        results = dict()

        for word in self.splitter(words):
                if word in results.keys():
                    results[word] = results[word] + 1
                else:
                    results[word] = 1

        #sorted_x = sorted(results.items(), key=operator.itemgetter(0))

        return results

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def map(self):
        all_words = dict()
        logging.debug("Starting mapper job")
        i=0
        try:
            for line in self.sysin:
                fields = line.split('\t')
                for f in fields:
                    line_words = self.splitter(f)
                    for w in line_words:
                        if self.word_list[0] in w:
                            i = i + 1
                            self.save_data(i, w)

        except Exception as ex:
            logging.error("An error has occurred:\n{0}\n".format(ex.message))
        finally:
            logging.debug("Mapping complete. Closing local mapper log file.")
            return all_words

#Do the work
if __name__ == "__main__":
    mapper = LengthMapper()
    mapper.word_list = ["fantasatic"]
    mapper.map()
