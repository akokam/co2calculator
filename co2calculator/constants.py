#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constant values
"""
import enum

KWH_TO_TJ = 277777.77777778


class BusinessTripTransportationMode(enum.Enum):
    CAR = 'Car'
    BUS = 'Bus'
    TRAIN = 'Train'
    PLANE = 'Plane'


class CommutingTransportationMode(enum.Enum):
    CAR = 'Car'
    BUS = 'Bus'
    TRAIN = 'Train'
    BICYCLE = 'Bicycle'
    EBIKE = 'E-bike'
    MOTORBIKE = 'Motorbike'
    TRAM = 'Tram'


class HeatingFuel(enum.Enum):
    HEAT_PUMP_AIR = 'Heat pump air'
    HEAT_PUMP_GROUND = 'Heat pump ground'
    HEAT_PUMP_WATER = 'Heat pump water'
    LIQUID_GAS = 'Liquid gas'
    OIL = 'Oil'
    PELLETS = 'Pellets'
    SOLAR = 'Solar'
    WOODCHIPS = 'Woodchips'
    ELECTRICITY = 'Electricity'
    GAS = 'Gas'
    COAL = 'Coal'
    DISTRICT_HEATING = 'District heating'


class ElectricityFuel(enum.Enum):
    GERMAN_ENERGY_MIX = "German energy mix"
    SOLAR = "Solar"


class CarBusFuel(enum.Enum):
    ELECTRIC = 'Electric'
    HYBRID = 'Hybrid'
    PLUGIN_HYBRID = 'Plug-in hybrid'
    CNG = 'CNG'
    GASOLINE = 'Gasoline'
    DIESEL = 'Diesel'
    AVERAGE = 'Average'
    HYDROGEN = 'Hydrogen'


class Size(enum.Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    AVERAGE = 'Average'


class TrainFuel(enum.Enum):
    ELECTRIC = 'Electric'
    DIESEL = 'Diesel'
    AVERAGE = 'Average'


class FlightClass(enum.Enum):
    ECONOMY = 'Economy class'
    PREMIUM_ECONOMY = 'Premium economy class'
    BUSINESS = 'Business class'
    FIRST = 'First class'
    AVERAGE = 'Average'


class FerryClass(enum.Enum):
    FOOT = 'Foot passenger'
    CAR = 'Car passenger'
    AVERAGE = 'Average'


class FlightRange(enum.Enum):
    DOMESTIC = 'Domestic'
    SHORT_HAUL = 'Short-haul'
    LONG_HAUL = 'Long-haul'


class BusTrainRange(enum.Enum):
    LOCAL = 'Local'
    LONG_DISTANCE = 'Long-distance'

class Unit(enum.Enum):
    KWH = "kwh"
    KG = "kg"
    L = "l"
    M3 = "m^3"
