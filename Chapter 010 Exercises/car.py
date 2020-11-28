# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 10 Exercise 2. Car Class
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self._speed = 0

    def get_year(self):
        pass

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed
