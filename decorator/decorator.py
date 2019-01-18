# -*- coding: utf-8 -*-
# @FileName: decorator.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

# component
class Beverage(object):
    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    def cost(self):
        pass

# concrete component
class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = "HouseBlend"

    def cost(self):
        return 1.99

# concrete component
class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.39

    def getDescription(self):
        return self.description

# decorator
class CondimentDecorator(Beverage):

    def getDescription(self):
        pass

# concrete decorator
class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super(Milk, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"

    def cost(self):
        return self.beverage.cost() + .2

# concrete decorator
class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .3


beverage = HouseBlend()
beverage = Milk(beverage)
beverage = Mocha(beverage)
print("{0}: {1}".format(beverage.getDescription(), "%.3f" % beverage.cost()))
