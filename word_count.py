WORD_COLLECTION = {}
def main():
    word_list = {}
    str_count = 0
    text = str(input("Give a sentence:"))
    for word in text.split():
        word_str = 0
        for char in word:
            word_str = word_str + 1
            if word_str > str_count:
                str_count = word_str
        if word in WORD_COLLECTION:
            WORD_COLLECTION[word] = WORD_COLLECTION[word] + 1
        else:
            WORD_COLLECTION[word] = 1
    word_list.update(WORD_COLLECTION)
    for item in sorted(word_list):
        print("{:{}} : {}".format(item, str_count, word_list[item]))

main()