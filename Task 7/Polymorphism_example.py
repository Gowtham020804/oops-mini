class Bird:

    def sound(self):
        print("Bird makes sound")


class Sparrow(Bird):

    def sound(self):
        print("Sparrow chirps")


class Parrot(Bird):

    def sound(self):
        print("Parrot talks")


# Polymorphism function
def make_sound(bird):
    bird.sound()


sparrow = Sparrow()
parrot = Parrot()

make_sound(sparrow)
make_sound(parrot)