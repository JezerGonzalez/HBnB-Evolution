class Country:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

country = Country("PuertoRico")
print(country.name)
try:
    country.name = "Francia"
except AttributeError as e:
    print(e)