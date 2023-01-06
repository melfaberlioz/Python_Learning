# оголошення змінної, яка згодом буде вставлена
# у іншу змінну через f-string, за допомогою якого у фігурних дужках
# можна буде вставляти потрібне значення змінної у потрібне місце
# іншої змінної.
types_of_people = 10
x = f"There are {types_of_people} types of people. "

# Оголошення змінних для наступної змінної х
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# виведення на екран стрінг х та у
print(x)
print(y)

# f-string використовується задля отримання можливості
# вставити іншу змінну всередину стрінга
print(f"I said: {x}")
print(f"I also said: '{y}'")

# булева функція
hilarious = False

# нова змінна
joke_evaluation = "Isn't that joke so funny?! {}"

# Виведення значення змінної joke_evaluation на екран,
# використавши вставлення всередину іншої змінної
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)