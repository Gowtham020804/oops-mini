
def even_numbers(limit):

    for i in range(limit):
        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)