
class HumanBeing(object):
    def __init__(self, firstName, lastName, eyeColor):
        self.firstName = firstName
        self.lastName = lastName
        self.eyeColor = eyeColor
        self.position = 0
        self.age = 0

    def walk_steps(self, steps):
        self.position += steps


def instantiateNewObjectHumanBeing():
    firstName = input("Enter first namw: ")
    lastName = input("Enter last name: ")
    eyeColor = input("Enter eye color: ")
    newHuman = HumanBeing(firstName, lastName, eyeColor)
    #print("Full name: {} {}".format(newHuman.firstName, newHuman.lastName))
    print("\Hello {} {}...".format(newHuman.firstName, newHuman.lastName))
    print("Eye color: {}".format(newHuman.eyeColor))

    numberSteps = input("Enter # steps: ")
    numberSteps = int(numberSteps)
    newHuman.walk_steps(numberSteps)
    print("New position: {}".format(newHuman.position))


class FinancialInstrument(object):
    author = "Erick Garcia"

    def __init__(self, exchange, symbol, price):
        self.symbol = symbol
        self.exchange = exchange
        self.__price = price

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price


def instantiateNewObjectFinancialInstrument():
    fi = FinancialInstrument("NASDAQ", "MSFT", 98)
    #print(type(fi))
    #print(fi)
    #fi.__price = 100

    aapl = FinancialInstrument("NASDAQ", "AAPL", 120)
    #print("Author: ", aapl.author)
    print("Exchange: {}, Ticker: {}, Price: {}".format(aapl.exchange, aapl.symbol, aapl.getPrice()))
    newPrice = input("Enter new price: ")
    newPrice = float(newPrice)
    aapl.setPrice(newPrice)
    print("Exchange: {}, Ticker: {}, Price: {}".format(aapl.exchange, aapl.symbol, aapl.getPrice()))
    return aapl


class PortfolioPosition(object):
    def __init__(self, FinancialInstrument, positionSize):
        self.position = FinancialInstrument
        self.__positionSize = positionSize

    def getPositionSize(self):
        return self.__positionSize

    def setPositionSize(self, positionSize):
        self.__positionSize = positionSize

    def getPositionValue(self):
        return self.__positionSize * self.position.getPrice()


def instantiateNewObjectPortfolioPosition():
    fi = instantiateNewObjectFinancialInstrument()
    pp = PortfolioPosition(fi, 10)
    print("\nAsset: {}, Price: {}, Position size: {}, Position value: {} ".format(\
        pp.position.symbol, pp.position.getPrice(), \
        pp.getPositionSize(), pp.getPositionValue()))


class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector (%r, %r, %r)" % (self.x, self.y, self.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __getitem__(self, i):
        if i == 0: return self.x
        elif i == 1: return self.y
        elif i == 2: return self.z
        else: return "Invalid index..."
        #else: raise IndexError("Index out of range.")


def instantiateNewObjectVector():
    v = Vector(1,2,3)
    print(v)
    print(abs(v))
    print(bool(v))
    print(v + Vector(2,3,4))
    print(v * 2)
    print(v[2])


#instantiateNewObjectHumanBeing()
#instantiateNewObjectFinancialInstrument()
#instantiateNewObjectPortfolioPosition()
instantiateNewObjectVector()
