class Grandfather:
    def car(self):
        return "Old car"


class Father(Grandfather):
    pass
    # def car(self):
    #     return "honda civic"


class Son(Father):
    # def car(self):
    #     return "Lambo"
    pass


son = Son()
print(son.car())