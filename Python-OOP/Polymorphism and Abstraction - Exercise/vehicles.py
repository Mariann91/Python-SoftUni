from abc import ABC, abstractmethod


class Vehicle(ABC):
  @abstractmethod
  def drive(self):
    pass

  @abstractmethod
  def refuel(self):
    pass

class Car(Vehicle):

  ADDED_FUEL_CONSUMPTION = 0.9
  
  def __init__(self, fuel_quantity, fuel_consumption):
    self.fuel_quantity = fuel_quantity
    self.fuel_consumption = fuel_consumption

  def drive(self, distance):
    total_fuel_consumption = (self.fuel_consumption + Car.ADDED_FUEL_CONSUMPTION) * distance

    if total_fuel_consumption <= self.fuel_quantity:
      self.fuel_quantity -= total_fuel_consumption

  def refuel(self, fuel):
    self.fuel_quantity += fuel

class Truck(Vehicle):

  ADDED_FUEL_CONSUMPTION = 1.6
  
  def __init__(self, fuel_quantity, fuel_consumption):
    self.fuel_quantity = fuel_quantity
    self.fuel_consumption = fuel_consumption
  
  def drive(self, distance):
    total_fuel_consumption = (self.fuel_consumption + Truck.ADDED_FUEL_CONSUMPTION) * distance
  
    if total_fuel_consumption <= self.fuel_quantity:
      self.fuel_quantity -= total_fuel_consumption
  
  def refuel(self, fuel):
    self.fuel_quantity += fuel * 0.95
    
