class Counter:
    def __init__(self, value = 0):
        # object attributes
        self.value = value

    # Methods
    def inc(self, step = 1):
        self.value += step

    def dec(self, step : int = 1):
        self.value -= step

    def getvalue(self):
        return self.value

# Create an object of Counter class
c = Counter()   # __init__(c)
c.inc(2)
c.inc()
print(c.getvalue())
print(c.value)

c2 = Counter(100)   # __init__(c2, 100)
c2.inc()
c2.dec()
print(c2.getvalue())