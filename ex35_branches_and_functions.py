from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">>> ")
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        print("Man, learn to type a number.")

    if how_much < 50:
        print('Nice< you\'re not greedy, you win')
        exit(0)
    else:
        print('You are greedy bastard!')


def bear_room():
    print('There is a bear here.\n The bear has a bunch of honey.\n The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        choice = input('>>> ')

        if choice == 'take honey':
            print('The bear looks at you then slaps your face off.')
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear has moved from the door. \n You can go through it now.')
            bear_moved = True

        elif choice == 'taunt bear' and bear_moved:
            print('The bear gets pissed off and chews your legs off.')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.\n"
          "He, it, whatever stares at you and you go insane.\n"
          "Do you flee for your life or eat your head?")

    choice = input('>>> ')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        print('Well that was tasty!')
    else:
        cthulhu_room()


def dead(why):
    print(why, 'Good job!')
    exit(0)


def start():
    print("You are in a dark room.\n"
          "There is a door to your right and left.\n"
          "which one do you take?")
    choice = input('>>> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        print('You stumble around the room until you starve.')


start()
