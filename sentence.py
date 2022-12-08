import string


class CreateList():

    def __init__(self, sent=str()):
        # w_lst = []
        self.__s = sent
        for i in string.punctuation:
            self.__s = self.__s.replace(i, '')
        # print(self.__s)
        w_lst = self.__s.split()
        print(w_lst)
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
        str = "I want to eat a piece of chicken."
        string = CreateList(str)
        # return __init__()
        return string

    def get_word(self):
        pass


def set_word():
    pass


def scramble():
    pass


if __name__ == "__main__":
    x = CreateList()
    print(x.get_all_words())
