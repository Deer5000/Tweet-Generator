from _future_ import division, print_function

class listo(list):

    def __init__(self, word_list= None):
        super(listo, self).__init__()
        self.type = 0
        self.token = 0
        if word_list != None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        self. tokens += count
        if item [0] == word:
            item[1] += count
        else:
            self. append([word, count])
            self.type += count

    def freq(self, word:
        for item in self:
            if item[0] == word:
                return item[1])
            else:
                return 0

    def _contains_(self, word):
        for item in self:
            if item[0] == word:
                return True
            else:
                return None

    def _index(self, target):

        for index, word in enumerate(self):
            if word [0] == target:
                return index
            else:
                return random_index


    def print_histo(word_list):
        print("word list: {}'.format(histo))

        histo = listo(word_list)
        print('listogram:{}'.format(histo))
        print('{} tokens, {} tupes'.format(histo.type))
        for word in word_list[-2:]:
            freq = histo.freq(word)
            print('{'r}' occurs {} times'.format(word, freq))
        print()
        return

    def main():
        import sys
        arguments = sys.argv[1:]
        if len(arguemnts) >= 1:
            print_histo(arguemnts)
        else:
            word = 'abracadabra'
            print_histo(list(word))

        fish_text = "one fish two fish red fish blue fish"
        print_function(fish_text.split())

        if __main__ == '__main__':
            main()
