from sys import argv

script, user_name = argv

# prompt дає нам можливість вводити свій інпут, бо для цього
# має бути щось, а не просто порожні дужки. І ми ставило цей знак >
# для того, щоб дати користувачу можливість ввести нові дані за запитом.
# але я не впевнена , що це так працює.
# Якщо приберемо prompt, то щось нічого особливо не міняється і інпут все одно вводиться.
prompt= bird = '<> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask a few more questions.")
print(f"Do you like me {user_name}?")
likes = input(bird)

print(f"Where do you live {user_name}?")
lives = input(bird)

print("What kind of computer do you have?")
computer = input(bird)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")