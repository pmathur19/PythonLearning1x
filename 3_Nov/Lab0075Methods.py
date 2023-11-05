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

    def sleep(self, timing):
        print("sleep for "+ str(timing))

    def walk(self):
        return "I am walking " + self.name  # accessing attribute of class in method

    def firstname(self):
        return "My first name is " + self.name


priyesh_obj_ref = Person()
priyesh_obj_ref.name = "priyesh"
print(priyesh_obj_ref.walk())
print(priyesh_obj_ref.firstname())
priyesh_obj_ref.sleep(5)
