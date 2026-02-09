class Cricket:
     x=100
s = Cricket()
print(s.x)

class Car:

    def __init__(self, model,year):
        self.model = model
        self.year = year

s = Car("Ferrari",2025)

print(s.model)
print(s.year)