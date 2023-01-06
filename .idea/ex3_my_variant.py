print("I will count my books:")

print("Scince fiction:", 3 * 18)
print("Novels:", 18 + 17 % 2)

print("Now I will count books I've read:")

#спочатку тут відбувається ділення 15/12, знак % означає остачу,
# тобто нам не дають результат ділення. Ми отримуємо остачу від ділення,
# себто 3, бо 15/12 = 1, і остача з ділення 3. Ця мат. операція є першочерговою.
# Далі програма віднімає остачу 3 від суми 54+19, і ми отримаємо відповідь: 70
print(54 + 19 - 15 % 12)

print("Is it true that I've read more books than haven't?")

print( 54+19 < 70)

print("Is it less?", 54+19 < 70)
print("Is it greater or equal?", 54+19 >= 70)
print("Is it less or equal?", 54 +19 <= 70)