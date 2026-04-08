from utils import BaseUtility

class StringOperations(BaseUtility):

    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def reverse_string(self):
        return self.text[::-1]

    def display(self):
        print("String Operations")
        print("Upper:", self.to_upper())
        print("Reverse:", self.reverse_string())


def count_words(sentence):
    return len(sentence.split())