# -*- coding: utf-8 -*-
# @FileName: hookBarista.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class CaffeineBeverageWithHook(object):
    """
    abstract class
    """
    def __init__(self):
        return

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
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

    def customerWantsCondiments(self):
        return True

class CoffeeWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        super(CoffeeWithHook, self).__init__()
        return

    def brew(self):
        print "Dripping Coffee through filter"

    def addCondiments(self):
        print "Adding Sugar and Milk"

    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer:
            return True
        else:
            return False

    def getUserInput(self):
        print "Would you like milk and sugar with your coffee (y/n)? "
        ans = raw_input("<<< Here (y/n) ?")
        if ans == 'y' or ans == 'Y':
            return True
        else:
            return False

class TeaWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        super(TeaWithHook, self).__init__()
        return

    def brew(self):
        print "Steeping the tea"

    def addCondiments(self):
        print "Adding Lemon"

    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer:
            return True
        else:
            return False

    def getUserInput(self):
        print "Would you like lemon with your tea (y/n)? "
        ans = raw_input("<<< Here (y/n) ?")
        if ans == 'y' or ans == 'Y':
            return True
        else:
            return False



tea = TeaWithHook()
coffee=CoffeeWithHook()
print "\nMaking tea..."
tea.prepareRecipe()
print "\nMaking coffee..."
coffee.prepareRecipe()
