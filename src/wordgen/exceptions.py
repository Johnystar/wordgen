class WordFilterError(Exception):
    pass


class WordTooShortError(WordFilterError):
    pass

class DuplicateWordError(WordFilterError):
    pass

class BannedSymbolsError(WordFilterError):
    pass
