class SuperHero:

    def __init__(self):
        print("Creating a new super hero...")

    def fly(self):
        print("I'm Flying!")

    def speed(self):
        print("Initiate Ludicrous Speed!")

    def forceSpeed(self, name):
        print(f'{name} crashed and burned...')

superman = SuperHero()
batman = SuperHero()
spiderman = SuperHero()

superman.fly()
spiderman.speed()
batman.forceSpeed("The Joker")
