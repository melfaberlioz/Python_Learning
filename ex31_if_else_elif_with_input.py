print("""You enter a dark room with two dors.
Do you go through door #1 or door #2?""")

door = input(">>> ")

if door == '1':
    print('There\'s a giant bear here eating a cheese cake.')
    print('What do you do?')
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">>> ")

    if bear == '1':
        print('The bear eats your face off. Good job!')
    elif bear == '2':
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('>>> ')

    if insanity == '1' or insanity =='2':
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity =='3':
        print("You have another choice. I want you to decide:")
        print('1. Стати москалем на один день, хоча ти нащадок Котляревського.')
        print('2. Померти в муках.')
        print("3. Каденція Порошенка буде вічною.")

        roshen = input(">>> ")

        if roshen == '1':
            print('Ти клятий московит, дарма тебе українська земля носить!!!')
        elif roshen == '2' or roshen =='3':
            print("Непоганий вибір, все краще, ніж бути москалем.")
        else:
            print("Будь-який вибір кращий, аніж бути москалем.2")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")