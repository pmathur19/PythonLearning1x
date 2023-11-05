#Create a Class Person , Two Objects by taking (name, age, address)
# Input from users and print details in the end.

class Person:
    name = None
    age = None
    address = None
    def task(self):
     print("Name = ", self.name)
     print("Age = ", self.age)
     print("Address = ", self.address, "\n")



p_obj = Person()
p_obj.name = input("Enter the Person Name : ")
p_obj.age = input("Enter the Person Age : ")
p_obj.address = input("Enter the Person Location : ")
p_obj.task()
print("--------------------------------------------------------------------")
m_obj = Person()
m_obj.name = input("Enter the Second person Name :")
m_obj.age = input("Enter the second Person Age : ")
m_obj.address = input("Enter the second person Location :")
m_obj.task()