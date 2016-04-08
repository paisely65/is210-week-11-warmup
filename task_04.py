#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses subclasses to demonstrate the has-a and is -a concepts."""

import car


class CustomCar(car.Car):
    """Another version of the car class.

    Attributes:
        None.
    """
class CustomTire(car.Tire):
    """A subclass of Tire for CustomTire

    Attributes:
        None.
    """

    def __init__(self, miles=0, tires = 4):
        """The class creator for CustomTire.

    def __init__(self, color = None, tires = None, cars = 1):
        """This class shows how to custom build cars.

        Args:
            color (string): color of car
            cars( int): Cars to be created. Default = 1

        Attributes:
            tires(list): list of CustomTire objects (equal to 4)
        """
    if tires is None:
        self.tires = []
    for i in xrange(4):
                self.tires.append(CustomTire(i-i))
    else:
        self.tires = tires




        Args:
            miles(int): The number of miles on tire. Default is 0.
            tires(int): The number of tires on the car

        Attributes:
            miles(int): The number of miles on the tire.
        """
        self.__maximum_miles = 500
