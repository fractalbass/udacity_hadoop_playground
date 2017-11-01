import operator

class word_counter():

    specialChar = ['.', ',', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-', '/', ' ']

    def process(self, words):

        results = dict()

        for phrase in words.split():
            for word in phrase.split():
                for c in self.specialChar:
                    word = word.replace(c, '')
                if word in results.keys():
                    results[word] = results[word] + 1
                else:
                    results[word] = 1

        sorted_x = sorted(results.items(), key=operator.itemgetter(1))

        return sorted_x
