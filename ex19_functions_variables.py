# Пишемо функцію def перед усім скриптом, адже в подальшому
# треба буде використовувати змінні, які мають вже
# бути позначені. Ми використовуємо створену нами функцію
# 'cheese_and_crackers' у рядку 15, і на той момент вона вже
# має існувати, адже зчитування Пайтона послідовне, зверху вниз.
# Рядки 7-11 ті, де ми створюємо функцію, що будемо використовувати надалі.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("Get a blanket.\n")

# Починаючи з рядка 16 код буде відображатися в компіляторі.
# Рядок 17 - виклик створеної у рядках 7-11 функції. У дужках
# зазначаємо аргументи-значення, які надаємо змінним cheese_count i boxes_of_crackers відповідно.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Тут ми використовуємо надання змінним значення окремо, через
# позначення кожної з них.
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

# В цьому рядку ми надаємо аргументам cheese_count i boxes_of_crackers
# еквівалетні змінні amount_of_cheese i amount_of_crackers.
# Тепер для функції вони тотожні за числовим значенням.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Викликаємо функцію і надаємо їй математичні операції замість
# вже порахованих значень аргументів cheese_count i boxes_of_crackers.
print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

# Використовуємо ототожнені з першозазначеними у ряду 28 значення
# для того, щоб виконати математичні операції, знову ж викликаючи
# створену нами у рядку 7-11 функцію.
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
