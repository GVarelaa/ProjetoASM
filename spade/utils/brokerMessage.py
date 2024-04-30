class brokerMessage():
    def __init__(self, decision, crypto, value, quantity, message):
        self.decision = decision
        self.crypto = crypto
        self.value = value
        self.quantity = quantity
        self.message = message
    
    def getDecision(self):
        return self.decision

    def getCrypto(self):
        return self.crypto
    
    def getValue(self):
        return self.value
    
    def getQuantity(self):
        return self.quantity
    
    def setDecision(self, decision):
        self.decision = decision
    
    def setCrypto(self, crypto):
        self.crypto = crypto
    
    def setValue(self, value):
        self.value = value
    
    def setQuantity(self, quantity):
        self.quantity = quantity
    
    def getMessage(self):
        return self.message
    
    def setMessage(self, message):
        self.message = message
       
    def __str__(self):
        return f"Decision: {self.decision}, Crypto: {self.crypto}, Value: {self.value}, Quantity: {self.quantity}"
    
    def __repr__(self):
        return f"Decision: {self.decision}, Crypto: {self.crypto}, Value: {self.value}, Quantity: {self.quantity}"
    
    

# podemos tentar usar isto pro manager pedir ao broker para comprar ou vender??