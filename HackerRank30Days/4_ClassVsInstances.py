class Person:
    def __init__(self, initialAge):
        self.initialAge = initialAge
        # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.initialAge < 13 and self.initialAge >= 0:
            print("You are young.")
        if self.initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
            self.amIOld()
        if self.initialAge >= 13 and self.initialAge < 18:
            print("You are a teenager.")
        if self.initialAge >= 18:
            print("You are old.")

        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        # print("increase in age->"+str(self.initialAge))
        self.initialAge = self.initialAge + 1
        # Increment the age of the person in here


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")