from .city import City
class City:
    
    def __init__(self, name):
        """Initialize with a name"""
        self.name = name

class Country:
    """Defines a country"""
    
    def __init__(self, name):
        """Initialize with a name"""
        self.name = name
        self.cities = []
        self.__cities = []

    def add_city(self, city):
        """Add a city"""
        if not isinstance(city, City):
            raise TypeError("The city must be an instance of the City class")
        self.cities.append(city)

    @property
    def name(self):
        """Get the name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the name"""
        if not isinstance(value, str):
            raise ValueError("The name must be a string")
        if not value.strip():
            raise ValueError("The name cannot be blank")
        self.__name = value

# Ejemplo de uso
try:
    country = Country("Spain")
    city = City("Madrid")
    country.add_city(city)  # Esto debería funcionar correctamente
    country.add_city("Barcelona")  # Esto debería lanzar un TypeError
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
