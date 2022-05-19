class land():
    def __init__(self, length,bredth,sqr_price):
        self.length = length
        self.bredth = bredth
        self.sqr_price = sqr_price

    @classmethod
    def empty(cls):
        return cls(0,0,0)

    def __str__(self):
        return 'length = ' +str(self.length) +' bredth = '+str(self.bredth)

    def __repr__(self):
        return "this is object of class land, "

l1 = land(10,20,300)
l2 = land.empty()
print(repr(l1),l1)
