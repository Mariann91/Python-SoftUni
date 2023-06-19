class Town:
  def __init__(self, name):
    self.name = name
    self.latitude = "0°N"
    self.longitude = "0°E"

  def set_latitude(self, current_latitude):
    self.latitude = current_latitude
  
  def set_longitude(self, current_longitude):
    self.longitude = current_longitude

  def __repr__(self):
    return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
