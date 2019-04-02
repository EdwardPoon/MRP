# Define a function
def world():
    print("Hello, World!")

# Define a variable
shark = "Sammy"


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    return z
    


# Define a class
class Octopus:
    animal_type = "Octopus" # Class Variables which would be shared by all instances
    location = "ocean"
    followers = 5
    def __init__(self, name, color):
        self.color = color   # instances Variable
        self.name = name

    def tell_me_about_the_octopus(self):
        print("This octopus is " + self.color + ".")
        print(self.name + " is the octopus's name.")