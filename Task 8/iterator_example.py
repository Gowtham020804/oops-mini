
class NumberIterator:

    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


numbers = NumberIterator(5)

for n in numbers:
    print(n)