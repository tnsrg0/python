class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = str(cost)
        self.track = str(track)

    def format_mailing(self):
        from_addr = self.from_address.full_address()
        to_addr = self.to_address.full_address()
        return f"Отправление {self.track} из {from_addr} в {to_addr}. \
Стоимость {self.cost} рублей."
