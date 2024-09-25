from translate import Translator

class Dictionary:
    def __init__(self):
        self._dict = {}

    def add_word(self, word:str, meaning:str):
        self._dict[word] = meaning

    def remove_word(self, word):
        if word in self._dict:
            del self._dict[word]

    def update_word(self, word, meaning):
        if word in self._dict:
            self._dict[word] = meaning

    def search(self, word):
        for i in self._dict:
            if word == i:
                print(f"Meaning of {i}: {self._dict[i]}")
            else:
                print("Not update yet")


class Bilingual_dict(Dictionary):
    def __init__(self, language="vi"):
        super().__init__()
        self._language = language
        self._translator = Translator(to_lang=self._language)

    def search(self, word):     # Override search to print the announcement in each other language
        if word in self._dict:
            announcement = self._translator.translate("Meaning of")
            print(f"{announcement} {word}: {self._dict[word]}")
        else:
            print(self._translator.translate("Not updated yet"))


class Technical_dict(Bilingual_dict):
    def __init__(self, language="vi", field="general"):
        super().__init__(language)
        self._field = field

    def add_word(self, word: str, meaning: str):
        self._dict[word] = f"{meaning} (Field: {self._field})"

    def search(self, word):  # Override search to include technical field
        if word in self._dict:
            announcement = self._translator.translate("Meaning of")
            print(f"{announcement} {word}: {self._dict[word]}")
        else:
            print(self._translator.translate("Not updated yet"))


class Synonyms_dict(Dictionary):
    def __init__(self):
        super().__init__()

    def add_word(self, word, sylist:list):
        self._dict[word] = sylist

    def add_synonyms(self, word, synonyms):
        self._dict[word].append(synonyms)

    def search(self, word):
        for i in self._dict:
            if word == i:
                if type(self) == Synonyms_dict:
                    print(f"Synonyms of {i}: {self._dict[i]}")
                if type(self) == Antonyms_dict:
                    print(f"Antonyms of {i}: {self._dict[i]}")
            else:
                print("Not update yet")

class Antonyms_dict(Synonyms_dict):
    pass


class History_search:
    def __init__(self):
        self._search_history = []

    def history(self, word):
        self._search_history.append(word)

    def view_history(self):
        print("Search History:")
        for i, word in enumerate(self._search_history, start=1):  # Use enumerate to get index and word
            print(f"{i}. {word}")




bilingual_dict = Bilingual_dict(language="vi")
technical_dict = Technical_dict(language="vi", field="engineering")
synonyms_dict = Synonyms_dict()
antonyms_dict = Antonyms_dict()
history = History_search()



# Add
bilingual_dict.add_word("house", "nhà")
bilingual_dict.add_word("car", "xe")
bilingual_dict.add_word("book", "sách")
# Search
bilingual_dict.search("house")
bilingual_dict.search("pen")  # Not added yet
history.history("house")


# Add
technical_dict.add_word("algorithm", "thuật toán")
technical_dict.add_word("circuit", "mạch điện")
# Search
technical_dict.search("algorithm")
technical_dict.search("resistor")  # Not added yet
history.history("algorithm")


# Add
synonyms_dict.add_word("happy", ["cheerful", "joyful", "delighted"])
synonyms_dict.add_synonyms("happy", "content")
# Search
synonyms_dict.search("happy")
synonyms_dict.search("sad")  # Not added yet
history.history("happy")


# Add
antonyms_dict.add_word("good", ["bad", "awful", "unpleasant"])
antonyms_dict.add_synonyms("good", "terrible")
# Search
antonyms_dict.search("good")
antonyms_dict.search("evil")  # Not added yet
history.history("good")



# View search history
print("\n-- Search History --")
history.view_history()
