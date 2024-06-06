import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, new_name=None):
        if new_name:
            self.name = new_name
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return (f"Country(id={self.id}, name='{self.name}', "
                f"created_at='{self.created_at}', updated_at='{self.updated_at}')")

# Example usage
country = Country(name="Exampleland")
print(country)

# Updating the country name
country.update(new_name="New Exampleland")
print(country)
