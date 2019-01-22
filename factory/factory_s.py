# -*- coding: utf-8 -*-
# @FileName: factory_s.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class SimplePizzaFactory(object):
    def __init__(self):
        return

    def createPizza(self, type):
        pizza = None
        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'clam':
            pizza = ClamPizza()
        elif type == 'pepperoni':
            pizza = PepperoniPizza()
        elif type == 'veggie':
            pizza = VeggiePizza()

        return pizza

class PizzaStore(object):
    def __init__(self, factory):
        self.factory = factory

    def orderPizza(self, type):
        pizza = self.factory.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


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

    def bake(self):
        print "Baking " + self.name

    def cut(self):
        print "Cutting " + self.name

    def box(self):
        print "Boxing" + self.name

class CheesePizza(Pizza):
    def __init__(self):
        super(CheesePizza, self).__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"


class ClamPizza(Pizza):
    def __init__(self):
        super(ClamPizza, self).__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin crust"
        self.sauce = "White garlic sauce"


class PepperoniPizza(Pizza):
    def __init__(self):
        super(PepperoniPizza, self).__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"


class VeggiePizza(Pizza):
    def __init__(self):
        super(VeggiePizza, self).__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"



factory = SimplePizzaFactory()
store = PizzaStore(factory)
pizza = store.orderPizza("cheese")
print pizza.getName()