# -*- coding: utf-8 -*-
# @FileName: decorator_2.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class Beverage(object):
    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    def cost(self):
        pass

    def getSize(self):
        return self.size

    def setSize(self, cupSize):
        self.size = cupSize

class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = "HouseBlend"

    def cost(self):
        if self.getSize() == "TALL":
            return 1.99
        elif self.getSize() == "GRANDE":
            return 2.99
        elif self.getSize() == "VENTI":
            return 3.99

# decorator
class CondimentDecorator(Beverage):

    def getDescription(self):
        pass

class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super(Milk, self).__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"

    def cost(self):
        if self.beverage.getSize() == "TALL":
            return self.beverage.cost() + .2
        elif self.beverage.getSize() == "GRANDE":
            return self.beverage.cost() + .25
        elif self.beverage.getSize() == "VENTI":
            return self.beverage.cost() + .30

beverage = HouseBlend()
beverage.setSize("VENTI")
beverage = Milk(beverage)
print("{0}: {1}".format(beverage.getDescription(), "%.3f" % beverage.cost()))