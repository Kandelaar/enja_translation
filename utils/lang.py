import unicodedata
import re

UNK_token = 3
SOS_token = 2
EOS_token = 1
PAD_token = 0


class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {'[SOS]': 2, '[EOS]': 1, '[PAD]': 0, '[UNK]': 3}
        self.index2word = {2: '[SOS]', 1: '[EOS]', 0: '[PAD]', 3: '[UNK]'}
        self.vocab_size = 4
        self.word_cnt = {}

    def scan_sentence(self, sentence):
        for word in sentence.split(' '):
            self.scan_word(word)

    def scan_word(self, word):
        if word not in self.word2index.keys():
            self.word2index[word] = self.vocab_size
            self.index2word[self.vocab_size] = word
            self.word_cnt[word] = 1
            self.vocab_size += 1
        else:
            self.word_cnt[word] += 1




def unicode2ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize_string(s):
    s = unicode2ascii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s


def normalize_two_sentence(s1, s2):
    return [normalize_string(s1), normalize_string(s2)]
