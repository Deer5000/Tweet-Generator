from __future__ import division, print_function


class Listo(list):

    def __init__(self, word_list=None):
        super(Listo, self).__init__()
        self.tokens = 0 
        if word_list is not None:
            for word in word_list:
                self.add_count(word)


    def add_count(self, word, count=1):
        for pair in self:
            if pair[0] == word:
                pair[1] += count
                self.tokens += count
                self.types = self.__type__()
                return

        self.tokens += count
        pair = [word, count]
        self.append(pair)
        self.types = self.__type__()



    def __type__(self):
        return len(self)


    def frequency(self, word):
        if not self.__contains__(word):
            return 0
        else:
            index = self.index_of(word)
            return self[index][1]

    def __contains__(self, word):

        for word_list in self:
            if word == word_list[0]:
                return True
        return False

    def index_of(self, target):
        index = 0
        for word_list in self:
            if word_list[0] == target:
                return index
            index += 1
        return index


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    histogram = Listo(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        print_histogram(arguments)
    else:
        word = 'abracadabra'
        print_histogram(list(word))
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

if __name__ == '__main__':
    main()
