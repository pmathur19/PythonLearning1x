def SayHello(name):
    print("welcome to class :",name)

sayHelloLambda = lambda name: print("welcome to class :",name)

name1 = "priyesh"
print(SayHello(name1))
print(sayHelloLambda(name1))