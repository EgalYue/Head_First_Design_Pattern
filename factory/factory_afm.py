# -*- coding: utf-8 -*-
# @FileName: factory_afm.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

# abstract class
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
        pizza = None
        ingredientFactory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("New York Style Cheese Pizza")
        # elif item == 'veggie':
        #     return NYStyleVeggiePizza()
        # elif item == 'clam':
        #     return NYStyleClamPizza()
        # elif item == 'pepperoni':
        #     return NYStylePepperoniPizza()
        else:
            pizza = None

        return pizza

# interface
class PizzaIngredientFactory(object):
    def __init__(self):
        return

    def createDough(self):
        return

    def createSauce(self):
        return

    def createCheese(self):
        return

    def createVeggies(self):
        return

    def createPepperoni(self):
        return

    def createClam(self):
        return


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        return

    def createDough(self):
        return ThinCrustDough()

    # def createSauce(self):
    #     return MarinaraSauce()
    #
    # def createCheese(self):
    #     return ReggianoCheese()
    #
    # def createVeggies(self):
    #     return
    #
    # def createPepperoni(self):
    #     return SlicedPepperoni()
    #
    # def createClam(self):
    #     return FreshClams()


# interface
class Dough(object):
    def __init__(self):
        return


class ThinCrustDough(Dough):
    def __init__(self):
        print "Thin Crust Dough"

# abstract class
class Pizza(object):

    def __init__(self):
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.cheese = ''
        self.Pepperoni = ''
        self.clam = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def prepare(self):
        return

    def bake(self):
        print "Baking " + self.name

    def cut(self):
        print "Cutting " + self.name

    def box(self):
        print "Boxing" + self.name



class CheesePizza(Pizza):

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print "Preparing " + self.name
        self.dough = self.ingredientFactory.createDough()
        # self.sauce = ingredientFactory.createSauce()
        # self.cheese = ingredientFactory.createCheese()



nyStore = NYPizzaStore()
pizza = nyStore.orderPizza("cheese")
