import re

class WordCloudData(object):


    def __init__(self, input_string: str):
        self.words_to_counts = {}
        self.bla = re.sub('\W+', ' ', input_string.lower()).split()
        for word in self.bla:
            self.words_to_counts[word] = (self.words_to_counts.get(word) or 0) + 1

    def __str__(self):
        return str(self.bla)


word = WordCloudData('I like cake')

print (word.words_to_counts)