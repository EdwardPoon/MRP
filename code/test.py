
import random


# Define cars variable as a list of strings
cars = ['BMW', 'benz', 'audi', 'volvo', 'opel', 'subaru']

# For loop that iterates over cars list and prints each string item
for car in cars:
   print(car)

# tuple: which use parentheses ( ) instead of square brackets are immutable ,their values cannot be modified
animals = ('cat', 'dog', 'elephant', 'tiger', 'lion', 'fish')
print(animals)

# dictionary: build-in map
sammy = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue',  'location': 'ocean'}
print(sammy)
print(sammy['color'])

for i in range(0, -10, -2):
   print(i)

print("Sammy" * 9)
print("Sammy" + " Andy")
# there are two ways to include " in string as followed
print('Sammy says, "Hello!"')
print("Sammy says, \"Hello!\"")


# print multiple lines:
print("""
hello
hi
""")
# can use \n as line break as well
print("\t hello \n hi")

# A raw string starting with r tells Python to ignore all formatting within a string, including escape characters.
print(r"Sammy says,\"The balloon\'s color is red.\"")

new_open_string = "Sammy loves {} {}." 
new_open_string2 = "Sammy loves {1} {0}."      # define the order      
print(new_open_string.format("open-source", "software"))
print(new_open_string2.format("open-source", "software"))

print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))


print(",".join(["sharks", "crustaceans", "plankton"]))

# convert
f = 57
print(float(f)) # convert int to float
print(str(f))


words = 8       # How many words in our book
per_page_A = 3    
per_page_B = 2    

print(divmod(words,per_page_A)) # Calculate Option A
print(divmod(words,per_page_B)) # Calculate Option B


def new_shark():
    #Assign variable as global
    global shark
    shark = "shark"

#Call new_shark() function
new_shark()

#Print global variable shark
print(shark)


print((-0.2 > 1.4) and (0.8 < 3.1)) # One original expression is False
print((7.5 == 8.9) or (9.2 != 9.2)) # Both original expressions are False       
print(not(-5.7 <= 0.3))   

balance = 1
if balance < 0:
    print("Balance is below 0, add funds now or you will be charged a penalty.")
elif balance == 0:
    print("Balance is equal to 0, add funds soon.")
else:
    print("Your balance is 0 or above.")


import org.prediction.example.classandfunction as classandfunction
# Call function
classandfunction.world()

# Print variable
print(classandfunction.shark)

# Call class
jesse = classandfunction.Octopus("Jesse", "orange")
eric = classandfunction.Octopus("eric", "blue")
jesse.tell_me_about_the_octopus()
jesse.animal_type = "fish"
print(jesse.animal_type)
print(eric.animal_type) # eric.animal_type is still optus 


print(classandfunction.multiply(4, 5))
print(classandfunction.multiply(10, 9))
print(classandfunction.multiply(2, 3, 4))
print(classandfunction.multiply(3, 5, 10, 6))

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")

# comment multiple lines
'''
number = random.randint(1, 25)

for i in range(1):
# while number_of_guesses < 5:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)

    # number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('You guessed the number!')

else:
    print('You did not guess the number. The number was ' + str(number))
'''