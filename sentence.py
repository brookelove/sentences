import string


class OutOfIndex (Exception):
    print(' ')


class Sentence:

    def __init__(self, sent=str()):
        # w_lst = []
        self.__s = sent
        for i in string.punctuation:
            self.__s = self.__s.replace(i, '')
        # print(self.__s)

        # print(w_lst)
        # return w_lst
        # s_lst = list(self.__s)
        # print(s_lst)
        # for i in self.__s:
        # print(i)
        # if i not in string.punctuation:
        # print(i)
        # w_lst.append(i)
        # i.pop(-1)
        # w_lst.append(i)

        # w_lst.append(i)
        # print(w_lst)

    def get_all_words(self):
        # return __init__()
        w_lst = self.__s.split()
        return w_lst

    def get_word(self, w_lst, desired_w):
        print(len(w_lst))
        if int(desired_w) > len(w_lst)-1:
            raise OutOfIndex
        else:
            return w_lst[desired_w]


def set_word():
    pass


def scramble():
    pass


if __name__ == "__main__":
    sent = 'I want to eat chicken and sleep for three years. I wish I had a cat named Smoke!'
    x = Sentence(sent)
    get_words = x.get_all_words()
    print(get_words)
    get_one_word = x.get_word(get_words, 1)
    # print(get_one_word)
