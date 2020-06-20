from utils.lang import *


def read_data(reverse=False):
    print('Reading ...')

    eng_lines = open('./data/train.en', encoding='utf-8').read().strip().split('\n')
    ja_lines = open('./data/train.ja', encoding='utf-8').read().strip().split('\n')

    pairs = []
    for i in range(len(ja_lines)):
        pairs.append([eng_lines[i], ja_lines[i]])

    input_lang = Lang('eng')
    output_lang = Lang('ja')

    if reverse:
        input_lang = Lang('ja')
        output_lang = Lang('eng')

    return input_lang, output_lang, pairs


def read_dev_test(reverse=False):
    print('Reading ...')

    eng_lines = open('./data/dev.en', encoding='utf-8').read().strip().split('\n')
    ja_lines = open('./data/dev.ja', encoding='utf-8').read().strip().split('\n')

    dev_pairs = []

    for i in range(len(ja_lines)):
        if not reverse:
            dev_pairs.append((eng_lines[i], ja_lines[i]))
        else:
            dev_pairs.append((ja_lines[i], eng_lines[i]))

    eng_lines = open('./data/test.en', encoding='utf-8').read().strip().split('\n')
    ja_lines = open('./data/test.ja', encoding='utf-8').read().strip().split('\n')

    test_pairs = []

    for i in range(len(ja_lines)):
        if not reverse:
            test_pairs.append((eng_lines[i], ja_lines[i]))
        else:
            test_pairs.append((ja_lines[i], eng_lines[i]))

    return dev_pairs, test_pairs
