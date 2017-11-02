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
            words = words.replace(c, ' ')
        split = words.split()
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
        self.sysout.write("{1}\t->{0}<-\n".format(key, value))

    def map(self):
        all_words = dict()
        logging.debug("Starting mapper job")
        try:
            for line in self.sysin:
                fields = line.split('\t')
                if len(fields) > 4:
                    for k in self.word_list:
                        if k in fields[4]:
                            line_words = self.process(fields[4])
                            for w in line_words.keys():
                                if k in w:
                                    self.save_data(fields[0], w)

            # if len(all_words.keys()) > 0:
            #     for k in all_words.keys():
            #         self.save_data(k, all_words[k])

        except Exception as ex:
            logging.error("An error has occurred:\n{0}\n".format(ex.message))
        finally:
            logging.debug("Mapping complete. Closing local mapper log file.")
            return all_words

#Do the work
if __name__ == "__main__":
    mapper = LengthMapper()
    mapper.word_list = ["fantastic"]
    mapper.map()
