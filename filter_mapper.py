#!/usr/bin/python
import logging
import sys
import operator

sys.path.append('./')

class LengthMapper():

    logging.basicConfig(filename='mapper.log')

    sysin = sys.stdin
    sysout = sys.stdout

    specialChar = ['.', ',', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/']

    def clean_word(self, text):
        for c in self.specialChar:
            text = text.replace(c, '').lower()
        return text

    def process(self, words):

        results = dict()

        for phrase in words.split():
            for word in phrase.split():


                if word in results.keys():
                    results[word] = results[word] + 1
                else:
                    results[word] = 1

        #sorted_x = sorted(results.items(), key=operator.itemgetter(0))

        return results

    def save_data(self, key, value):
        self.sysout.write("{0}\t{1}\n".format(key, value))

    def map(self, word_list):
        all_words = dict()
        logging.debug("Starting mapper job")
        try:
            for line in self.sysin:
                fields = line.split('\t')
                if len(fields) > 4:
                    for k in word_list:
                        if k in fields[4]:
                            body = self.clean_word(fields[4])
                            line_words = self.process(body)

                            for w in line_words.keys():
                                if k in w:
                                    self.save_data(fields[0], w)


        except Exception as ex:
            logging.error("An error has occurred:\n{0}\n".format(ex.message))
        finally:
            logging.debug("Mapping complete. Closing local mapper log file.")

#Do the work
if __name__ == "__main__":
    mapper = LengthMapper()
    mapper.map(["fantastically"])
