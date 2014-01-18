from django.db import models

# Create your models here.

class Clothing(object):

    def __init__(self, gender=None, temp_min=None, temp_max=None, snow=False, 
                 sun=False, rain=False, is_extreme=True):
        self.gender = gender
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.snow = snow
        self.sun = sun
        self.rain = rain
        self.is_extreme = is_extreme
