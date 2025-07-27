#Creating class
class Cat:

    #creating constructor
    def __init__(self, name, age, breed):
        #Assigning the name to the object
        self.name = name
        self.age = age
        self.breed = breed
    
    #Creating Method(Behaviour or action)
    def meow(self):
        print("Meow! My name is {self.name}")
    def catinfo(self):
        print(self.name + " is " + str(self.age) + " Year(s) old and " + self.breed + " breed ")
    def is_senior(self):
        if self.age > 8:
            return "True"
        else:
            return "False"
        
#Asking user to input
num_cat = int(input("How many cat's: "))

#list to store cat object
cat_list = []

#Taking input from user
for i in range(num_cat):
    print(f"Enter the cat's Details #{i + 1}")
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    breed = input("Enter the breed: ")

    #creating object with user input and adding to list
    user_cat = Cat(name, age, breed)
    cat_list.append(user_cat)

#Displaying information
print("\n ---Cat Details--- ")
for c in cat_list:
    c.catinfo()
    print("Senior cat: ", c.is_senior(), "\n")