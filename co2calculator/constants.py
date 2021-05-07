#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constant values
"""

import enum

KWH_TO_TJ = 277777.77777778


class HeatingFuel(enum.Enum):
    PUMPAIR = 'Pump air'
    PUMPGROUND = 'Pump ground'
    PUMPWATER = 'Pump water'
    LIQUID = 'Liquid'
    OIL = 'Oil'
    PELLETS = 'Pellets'
    SOLAR = 'Solar'
    WOODCHIPS = 'Woodchips'
    ELECTRICITY = 'Electricity'
    GAS = 'Gas'


class ElectricityFuel(enum.Enum):
    GERMAN_ENERGY_MIX = "German energy mix"
    SOLAR = "Solar"


class CarFuel(enum.Enum):
    ELECTRIC = 'Electric'
    NATURAL = 'Natural'
    GAS = 'Gas'
    GASOLINE = 'Gasoline'
    DIESEL = 'Diesel'
    UNKNOWN = 'Unknown'


class Size(enum.Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    UNKNOWN = 'Unknown'


class TrainFuel(enum.Enum):
    ELECTRIC = 'Electric'
    DIESEL = 'Diesel'
    UNKNOWN = 'Unknown'


class FlightClass(enum.Enum):
    ECONOMY = 'Economy'
    BUSINESS = 'Business'
    FIRST = 'First'
    UNKNOWN = 'Unknown'