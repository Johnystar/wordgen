from random import randrange
from .exceptions import WordFilterError, WordTooShortError, DuplicateWordError, BannedSymbolsError, NotEnoughWordsError
from . import data


class Words():
    def __init__(self,
                 lower:bool=True,
                 min_length:int=2,
                 allowed_symbols:str='abcdefghijklmnopqrstuvwxyz') -> None:
        self.list = []
        self.lower = lower
        self.min_length = min_length
        self.allowed_symbols = allowed_symbols


    def get_n_words(self, amount:int) -> list[str]:
        if amount > len(self.list):
            raise NotEnoughWordsError("Not enough words available!")

        list_copy = self.list.copy()
        output = []

        while len(output) < amount:
            output.append(list_copy.pop(randrange(len(list_copy))))

        return output


    def get_words(self) -> list[str]:
        return self.list.copy()


    def add_word(self, word:str) -> None:
        if self.lower == True: word = word.lower()

        if len(word) < self.min_length: raise WordTooShortError("word too short")
        if word in self.list: raise DuplicateWordError ("word already in word list")
        if not all(char in self.allowed_symbols
                   for char in word): raise BannedSymbolsError("word contains banned symbols")

        self.list.append(word)


    def add_words(self, words:list[str]) -> None:
        for word in words:
            try:
                self.add_word(word)
            except WordFilterError as _:
                pass

def from_data(words:list[str]=["english"], course:str="colemak_DHm", level:int=1) -> Words:
    word_files = data.get_available_files("words")
    course_files = data.get_available_files("courses")
    
    word_list = [
        item for sublist in
        # the following list of lists get flattend
        # into a single word_list list of strings:
        [ data.parse_file(word_files[wordset]) for wordset in words ]
        for item in sublist
    ]
    course_list = data.parse_file(course_files[course])

    assert level >= 1
    assert level <= len(course_list)

    w = Words(
        allowed_symbols=''.join(course_list[:level])
    )

    w.add_words(word_list)

    return w
