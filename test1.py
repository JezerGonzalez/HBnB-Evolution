import uuid
from datetime import datetime

class Country:
    def __init__(self, name, code, capital):
        self._id = uuid.uuid4()  # Unique ID (UUID4)
        self._created_at = datetime.utcnow()  # Creation Date
        self._updated_at = datetime.utcnow()  # Update Date
        self._name = name
        self._code = code
        self._capital = capital

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._updated_at = datetime.utcnow()

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
        self._updated_at = datetime.utcnow()

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, value):
        self._capital = value
        self._updated_at = datetime.utcnow()

    def __repr__(self):
        return f"Country(id={self.id}, name={self.name}, code={self.code}, capital={self.capital}, created_at={self.created_at}, updated_at={self.updated_at})"

country = Country("United States", "USA", "Washington D.C.")
print(country)

# Update the country
country.name = "Estados Unidos"
country.capital = "Washington DC"
print(country)