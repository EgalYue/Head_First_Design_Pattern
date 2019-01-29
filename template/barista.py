# -*- coding: utf-8 -*-
# @FileName: barista.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class CaffeineBeverage(object):
    """
    abstract class
    """
    def __init__(self):
        return

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()

    def brew(self):
        # abstract
        return

    def addCondiments(self):
        # abstract
        return

    def boilWater(self):
        print "Boiling water"

    def pourInCup(self):
        print "Pouring into cup"


class Coffee(CaffeineBeverage):
    def __init__(self):
        super(Coffee, self).__init__()
        return

    def brew(self):
        print "Dripping Coffee through filter"

    def addCondiments(self):
        print "Adding Sugar and Milk"

class Tea(CaffeineBeverage):
    def __init__(self):
        super(Tea, self).__init__()
        return

    def brew(self):
        print "Steeping the tea"

    def addCondiments(self):
        print "Adding Lemon"



tea = Tea()
coffee=Coffee()
print "\nMaking tea..."
tea.prepareRecipe()
print "\nMaking coffee..."
coffee.prepareRecipe()