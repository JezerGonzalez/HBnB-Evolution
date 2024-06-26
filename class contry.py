
class Country:
    """Defines a country"""
    
    def __init__(self, name):
        """Initialize with a name"""
        self.name = name
        self.cities = []

    def add_city(self, city):
        """Add a city"""
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
