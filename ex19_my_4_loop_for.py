# define function
def get_square(num):
    # пропускаємо проміжну змінну і одразу вписуємо в
    # 'result' бажану математичну операцію.
    return num * num

# Створюємо цикл для змінної 'i', що набуває значень 1, 2, 3
for i in [1, 2, 3]:
    # Викликаємо функцію, одразу вписуючи її у рядок виведення 'result'
    # для отримання значень.
    result = get_square(i)
    print("Square of", i, '=', result)