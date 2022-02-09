from xml.sax.xmlreader import InputSource


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + '('+str(self.capacity) + 'L)')

    def __add__(self, other):
        new_juice = self.name +'&'+ other.name
        new_capacity = self.capacity + other.capacity
        return Juice(new_juice , new_capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b

print(result)
