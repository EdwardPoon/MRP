
# iteratable
mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

for i in mylist:
    print(i*2)

# generator use () instead of [], which can only be iterated once
mygenerator = (x * x for x in range(3))
for i in mygenerator:
   print(i)
for i in mygenerator:
   print(i*2)

# Yield is a keyword that is used like return, except the function will return a generator.
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

# when you call the function, the code you have written in the function body does not run
# your code will be run each time the for uses the generator.
mygenerator2 = createGenerator() # create a generator
print(mygenerator2) # mygenerator is an object!

for i in mygenerator2:
    print(i)

