import string
import random


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

    def get_word(self, index):
        # pass
        lst = self.get_all_words()
        # print(lst)
        # print(len(w_lst))
        # print(w_lst[desired_w])
        # this if block needs to go in if __name_ = "__main__" else would be the get_one_word statement
        if int(index) > len(lst)-1:
            return '" "'
        # print("wher is none")
        else:
            return lst[index]

    def set_word(self, index, new_word):  # need help with tis one
        # print(index, new_word)  # prints words
        # old_word = self.get_word(index)
        # return old_word[index]
        # sent.replace(index, new_word)
        # print(sent)
        # print(self.__s)
        # pass
        sent = self.__s
        old_word = self.get_word(index)
        return sent.replace(old_word, new_word)
        # return new_s

    def scramble(self):
        lst = self.get_all_words()
        scramble = random.sample(lst, len(lst))
        return scramble

    def __repr__(self) -> str:
        return self.__s + '.'


if __name__ == "__main__":
    sent = 'I want to eat chicken and sleep for three years. I wish I had a cat named Smoke!'
    x = Sentence(sent)
    lst = x.get_all_words()
    # print(get_words) # returns list of words
    index = 4
    # start sassertion error if the idnex is greater than the sentence
    assert index < len(lst)-1, f"' '"
    print(x.set_word(index, "potatoes"))
    # x.get_word(4)
    # x.set_word(4, "potatos")
    # x.scramble()
    # print(x.__repr__())
    # print("Sentence Unit test sucessful")
    # print(sent)
