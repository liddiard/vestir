from django.db import models

# Create your models here.

class Clothing(object):
    def __init__(self, gender=none, temp_min=none, temp_max=none, snow=false, sun=false, rain=false):
        self.gender = gender
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.snow = snow
        self.sun = sun
        self.rain = rain

class Footwear(Clothing):
    def __init__(self, **kwargs):
        super(Footwear, self).__init__(**kwargs)


class Tops(Clothing):
    def __init__(self, **kwargs):
        super(Tops, self).__init__(**kwargs)

class Bottoms(Clothing):
    def __init__(self, **kwargs):
        super(Bottoms, self).__init__(**kwargs)

class Accessories(Clothing):
    def __init__(self, **kwargs):
        super(Accessories, self).__init__(**kwargs)
