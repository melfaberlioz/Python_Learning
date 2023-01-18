# creating a class named 'BMTH'
class BMTH:
    # creating a function with __init__ that initialize my
    # newly created empty object. It requires to create objects.
    # __init__ identifies special methods, created by a programmer.
    # We use def to define a function or method, such as the __init__
    # method.
    # __init__ method initializes attribute 'lyric'.
    def __init__(self, song_lyric):
        # 'self' binds the object's attributes to the
        # arguments received.
        self.lyric = song_lyric

    def singing(self):
        for line in self.lyric:
            print(line)


# creating a new object (or instance) of the class 'BMTH'
# When we call 'sing_song', we first define the class from
# which it's created ('BMTH').
# Next we pass the list (in []) as an argument, which correspond
# to the respective parameters of the __init__ method of the class
# 'BMTH'
true_friends1 = ["I would've hold my breath",
                  "If I was you.",
                  "Cause I forget,",
                  "But I never forgive you.",]
true_friends2 = ["Don't you know,",
                    "Don't you know",
                    "True friends steb you in the front."]
sing_song = BMTH(true_friends1)
tragedy_end = BMTH(true_friends2)

sing_song.singing()
tragedy_end.singing()