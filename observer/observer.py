# -*- coding: utf-8 -*-
# @FileName: observer.py
# @Author  : Yue Hu
# @E-mail  : yue.hu@ninebot.com

class Subject(object):
    def __init__(self):
        print ">>> Subject interface "

    def registerObserver(self, observer):
        return

    def removeObserver(self, observer):
        return

    def notifyObserver(self, observer):
        return

class Observer(object):
    def __init__(self):
        print ">>> Observer interface"

    def update(self, temp, humidity, pressure):
        return

    def display(self):
        return


class WeatherData(Subject):
    def __init__(self):
        print ">>> WeatherData implements Subject "
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for obs in self.observers:
            obs.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMesurement(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionDisplay(Observer):
    def __init__(self, weatherData):
        print ">>> CurrentConditionDisplay implements Observer "
        self.weatherData = weatherData
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        weatherData.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print 'temprature = %f, humidity = %f, pressure = %f' % \
                (self.temperature, self.humidity, self.pressure)


weather = WeatherData()
display = CurrentConditionDisplay(weather)
weather.setMesurement(2.0, 3.0, 4.0)