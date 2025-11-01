def add(*args):
#    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum


#print(add(3,5,6, 10, 20))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
 #   print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(model="Mustang")
print(my_car.make)
print(my_car.model)