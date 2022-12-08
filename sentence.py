import string


class CreateList():

    def __init__(self, sent=str()):
        w_lst = []
        self.__s = sent
        # s_lst = list(self.__s)
        # print(s_lst)
        for i in self.__s:
            if i not in string.punctuation:
                w_lst.append(i)
        print(w_lst)

    def get_all_words():
        pass

    def get_word():
        pass


def set_word():
    pass


def scramble():
    pass


if __name__ == "__main__":
    str = "I want to eat a piece of chicken."
    string = CreateList(str)
    print(string)
