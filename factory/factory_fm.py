# -*- coding: utf-8 -*-
# @FileName: factory_fm.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class PizzaStore(object):
    def __init__(self):
        return

    def createPizza(self, item):
        return

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        print "--- Making a " + pizza.getName() + " ---"

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        # elif item == 'veggie':
        #     return NYStyleVeggiePizza()
        # elif item == 'clam':
        #     return NYStyleClamPizza()
        # elif item == 'pepperoni':
        #     return NYStylePepperoniPizza()
        else:
            return None


class Pizza(object):
    name = ''
    dough = ''
    sauce = ''

    def __init__(self):
        return

    def getName(self):
        return self.name

    def prepare(self):
        print "Preparing " + self.name
        print "ossing dough... "
        print "Adding sauce..."

    def bake(self):
        print "Baking " + self.name

    def cut(self):
        print "Cutting " + self.name

    def box(self):
        print "Boxing" + self.name


class  NYStyleCheesePizza(Pizza):
    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'


nyStore = NYPizzaStore()
pizza = nyStore.orderPizza("cheese")
print "Ethan ordered a " + pizza.getName()