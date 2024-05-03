class Asset:
    def __init__(self, coinid):
        self.coinid = coinid
        self.name = None
        self.quantity = None
        self.initial_price = None
        self.current_price = None
        self.value = None
        self.profit = 0

    def set_info(self, initial_price, quantity):
        self.quantity = quantity
        self.initial_price = initial_price
        self.current_price = initial_price
        self.value = quantity * initial_price

    def update(self, new_price):
        self.current_price = new_price
        self.value = self.quantity * new_price
        self.profit = (new_price - self.initial_price) * self.quantity


