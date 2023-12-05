class Car:
    name = "Pramod" # Class Varaible
#Constructor is Constructor is a  type of Method (Magic method ), jisme rakha hua code Automatic run hota haijb bhi uss class ka object banta hai
    def __init__(self,make,model): # Default con
        self.make = make  #  Instance Vairable are those fo which the value of the variabel is different for different objs
        self.model = model # Instance Vairable
        print("I will be called first")

    def start_engine(self):
        print("Starting a car", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine() #First will print the default constructor code, send will run the method for stating the engine
car2.start_engine()

print(id(car1)) #the ID of obj is same as the ID of Self in the constructor
print(id(car2)) # that means self is nothing but the object reference itself


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them