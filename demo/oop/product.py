class Product:
    taxrate = 12 # class attribute or static attribute
    def __init__(self, name, price):
        # Object attributes
        self.name = name
        self.price = price

    # Method
    @staticmethod
    def gettaxrate():
        return Product.taxrate

    def show(self):
        print("Name : ", self.name)
        print("Price : ", self.price)

    def getnetprice(self):
        return self.price + self.price * Product.taxrate // 100  # 12% tax


p1 = Product("iPhone 18 Pro", 90000)
print(p1.getnetprice())

print(Product.gettaxrate())
