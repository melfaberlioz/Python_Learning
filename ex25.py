def break_words(stuff):
    """This function will break up words for us.
    In 'words' ми використовуємо 'stuff.split(' ')'
    для того, щоб поставити туди функцію 'break_words'
    і у дужках зазначити змінну, у якій надане те речення,
    поділ якого ми бажаємо.
    Наприклад:
    sentence = "All good things come to those who wait."
    words = ex25.break_words(sentence)
    І згодом нам повертається значення, яке ми задали у 'words'  """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sort the words.
    Тут працює аналогічна схема. Використовуємо патерн, описаний
    у рядках 2-10.
    Наприклад:
    sorted_words = ex25.sort_words(words)
    - ми викликаємо функцію у створеній
    змінній "sorted_words". У ній викликаємо функцію '.sort_words',
    задаючи їй у дужках змінну, яку треба використовувати.
    У нашому випадку, це змінна 'words', яка була повернена під час
    виконання алгоритму у рядках 1- 12. Там речення вже розділене на слова,
    і тепер ми маємо можливість сортувати ці слова у теперішній функції.
    return зберігає/повертає значення, отримане під час виконання функції, а
    не висхідне значення. """
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it of.
    Створюємо нову змінну 'word', якій надаємо значення 'words.pop(0)' """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it of."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



# If we will write in the Terminal "from ex25 import *"
# it means we import everything from ex25" , hence later
# we have no need to write before every function 'ex25.'