# -*- coding: utf-8 -*-
# @FileName: simpleBarista.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class Coffee(object):
    def __init__(self):
        return

    def prepareRecipe(self):
        self.boilWater()
        self.brewCoffeeGrinds()
        self.pourInCup()
        self.addSugarAndMilk()

    def boilWater(self):
        print "Boiling water"

    def brewCoffeeGrinds(self):
        print "Dripping Coffee through filter"

    def pourInCup(self):
        print "Pouring into cup"

    def addSugarAndMilk(self):
        print "Adding Sugar and Milk"


class Tea(object):
    def __init__(self):
        return

    def prepareRecipe(self):
        self.boilWater()
        self.steepTeaBag()
        self.pourInCup()
        self.addLemon()

    def boilWater(self):
        print "Boiling water"

    def steepTeaBag(self):
        print "Steeping the tea"

    def addLemon(self):
        print "Adding Lemon"

    def pourInCup(self):
        print "Pouring into cup"


tea = Tea()
coffee = Coffee()
print "Making tea..."
tea.prepareRecipe()
print '----------------'
print "Making coffee..."
coffee.prepareRecipe()