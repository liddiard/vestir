import json
import urllib2

from django.views.generic import View
from django.http import HttpResponse, Http404

from vestir.settings.base import WUNDERGROUND_API_KEY


class ApiView(View):

    def json_response(self, **kwargs):
        return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
        return self.json_response(result=0, **kwargs)

    def error(self, error_type, message):
        return self.json_response(result=1, error=error_type, message=message)


class RecommendView(ApiView):
    
    def post(self, request):
        days = request.POST.get('days')
        gender = request.POST.get('gender')
        if dates is None:
            return self.error(error='KeyError', message='Required key (data) '
                              'not found in request.')
        if gender is None:
            return self.error(error='KeyError', message='Required key (gender) '
                              'not found in request.')
        for day in days:
            state = day.location.state
            city = '_'.join(day.location.city.split(' '))
            data = urllib2.urlopen('http://api.wunderground.com/api/%s/'
                                   'forecast10day/q/%s/%s.json') % \
                                   (WUNDERGROUND_API_KEY, state, city)
            jsn = json.load(data)
            return self.success(result=jsn)

#Footware
boots=Footwear(name="Boots", gender='b', temp_min=None, temp_max=70, sun=True,
               snow=True, rain=True, is_extreme=True)

sandals=Footwear(name="Sandals", gender='b', temp_min=75, temp_max=None, 
                 sun=True, snow=False, rain = False, is_extreme=False)

sneakers=Footwear(name="Tennis Shoes", gender='b', temp_min=50, temp_max=None, 
                  sun=True, snow=False, rain=False, is_extreme=False)
#Accessory
umbrella = Accessory(name="Umbrella", gender='b', temp_min=None, temp_max=None,
                     sun=False, snow=False, rain=True, is_extreme=True)

warm_hat = Accessories(name="Warm Hat",gender='b', temp_min=None, temp_max=60, 
                       sun=True, snow=True, rain=False, is_extreme=True)

scarf = Accessories(name="Scarf", gender='b', temp_min=None, temp_max=60, 
                    sun=True, snow=True, rain=True, is_extreme=False)
#Tops of outfits
tshirts = Tops(name="T-Shirt", gender='b', temp_min=65, temp_max=None,
               sun=True, snow=False, rain=True, is_extreme=False)

long_shirt = Tops(name="Long-Sleeved Shirt", gender='b', temp_min=None, 
                  temp_max=75, sun=True, snow=True, rain=True, is_extreme=True)

short_shirt = Tops(name="Short-Sleeved Shirt", gender='b', temp_min=35, 
                  temp_max=90, sun=True, snow=True, rain=True, is_extreme=False)
#Bottoms of outfits
jeans = Bottoms(name="Jeans", gender='b', temp_min=None, temp_max=95, 
                sun=True, snow=True, rain=True, is_extreme=True)

shorts = Bottoms(name="Long Sleeved Shirt", gender='b', temp_min=55, 
                  temp_max=None, sun=True, snow=False, rain=False, is_extreme=False)

thermal_underwear = Bottoms(name="Thermal Underwear", gender='b', temp_min=35, 
                  temp_max=75, sun=True, snow=True, rain=True, is_extreme=True)

#Jackets
heavy_coat = Jackets(name="Heavy Coat", gender='b', temp_min=None, 
                  temp_max=60, sun=True, snow=True, rain=True, is_extreme=True)

sweater = Jackets(name="Sweater", gender='b', temp_min=61, 
                  temp_max=78, sun=True, snow=True, rain=True, is_extreme=False)

wool_coat = Jackets(name="Heavy Wool Coat", gender='b', temp_min=None, 
                  temp_max=59, sun=True, snow=True, rain=False, is_extreme=True)

