class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = str(index)
        self.city = city
        self.street = street
        self.house = str(house)
        self.apartment = str(apartment)

    def full_address(self):
        result = f"{self.index} {self.city} {self.street}\
{self.house} - {self.apartment}"
        return result
