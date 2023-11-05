# Class and object

# Class Person
# Attributes - name, age , phone no, height weight, gender, profession
# methods - can do-> run(), sleep(), sing(), talk(), learn(), fight(), think()

class Person:
    # Attributes
    name = None
    age = None
    phone_n = None
    height = None
    weight = None
    gender = None
    profession = None   # if value is not assigned to variable u cannot use it

    # Methods
    def talk(self):
        print("talk")

    def sleep(self):
        print("sleepig")

    def walk(self):
        return "I am walking"


priyesh_obj = Person()
priyesh_obj.name = "Priyesh"
priyesh_obj.age = 30
priyesh_obj.phone_n = "63672262828"

print(priyesh_obj)   # this will print address of the object

priyesh_obj.sleep() # this will call the method

a_obj = Person()
a_obj.name = "Somesh"
print(a_obj) # address of the Object