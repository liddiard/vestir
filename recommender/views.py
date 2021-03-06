import json
import urllib2
import hashlib

from django.views.generic import View
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from vestir.settings.base import WUNDERGROUND_API_KEY
from .models import Clothing


class ApiView(View):

f =urlib2.urlopen('http://api.wunderground.com/api/13ca25e0144d7658/forecast10day/q/CA/San_Francisco.json')
json_string = f.read()
parsed_json = json.loads(json_string)
#location = parsed_json['location']['city']
#temp_f = parsed_json['forecast']['simpleforecast']['forecastday'][0]
count =0
for temp_f in parsed_json['forecast']['simpleforecast']['forecastday']:
            print count
                    temp_f = parsed_json['forecast']['simpleforecast']['forecastday'][count]
                            print temp_f
                                    count += 1
                                    f.close()

    def json_response(self, **kwargs):
            return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
        return self.json_response(result=0, **kwargs)

    def error(self, error, message):
        return self.json_response(result=1, error=error, message=message)


class RecommendView(ApiView):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RecommendView, self).dispatch(*args, **kwargs)
    
    def post(self, request):
        obj = json.loads(request.body)
        days = obj.get('days')
        gender = obj.get('gender')
        if days is None:
            return self.error(error='KeyError', message='Required key (days) '
                              'not found in request.')
        if gender is None:
            return self.error(error='KeyError', message='Required key (gender) '
                              'not found in request.')
        for day in days:
            try:
                state = day['location']['state']
            except KeyError:
                return self.error(error='KeyError', message='Required key '
                                  '(location.state) not found in request.')
            try:
                city = '_'.join(day['location']['city'].split(' '))
            except KeyError:
                return self.error(error='KeyError', message='Required key '
                                  '(location.city) not found in request.')
            url = "http://api.wunderground.com/api/%s/forecast10day/q/%s/%s.json" % \ 
                  (WUNDERGROUND_API_KEY, state, city)
            return self.json_response(url=url)
            data = urllib2.urlopen(url)
            jsn = json.load(data)
            print jsn

#Footwear
boots=Clothing(name="Boots", gender='b', temp_min=None, temp_max=70, sun=True,
               snow=True, rain=True, is_extreme=True)

sandals=Clothing(name="Sandals", gender='b', temp_min=75, temp_max=None, 
                 sun=True, snow=False, rain = False, is_extreme=False)

sneakers=Clothing(name="Tennis Shoes", gender='b', temp_min=50, temp_max=None, 
                  sun=True, snow=False, rain=False, is_extreme=False)

flipflop = Clothing(name="Flip-Flops", gender='b', temp_min=75, temp_max=None,
                    sun=True, snow=False, rain=False, is_extreme=False)
#Add footwear to list
footwear = [boots, sandals, sneakers, flipflop]
#Accessory
umbrella = Clothing(name="Umbrella", gender='b', temp_min=None, temp_max=None,
                     sun=False, snow=False, rain=True, is_extreme=True)

warm_hat = Clothing(name="Warm Hat",gender='b', temp_min=None, temp_max=60, 
                       sun=True, snow=True, rain=False, is_extreme=True)

scarf = Clothing(name="Scarf", gender='b', temp_min=None, temp_max=60, 
                    sun=True, snow=True, rain=True, is_extreme=False)

sunscreen = Clothing(name="Sunscreen", gender='b', temp_min=None, temp_max=None,
                     sun=True, snow=False, rain=False, is_extreme=False)
#Add Accessories to List
accessories = [umbrella, warm_hat, scarf, sunscreen]
#Tops of outfit
tshirts = Clothing(name="T-Shirt", gender='b', temp_min=65, temp_max=None,
               sun=True, snow=False, rain=True, is_extreme=False)

long_shirt = Clothing(name="Long-Sleeved Shirt", gender='b', temp_min=None, 
                  temp_max=75, sun=True, snow=True, rain=True, is_extreme=True)

short_shirt = Clothing(name="Short-Sleeved Shirt", gender='b', temp_min=35, 
                  temp_max=90, sun=True, snow=True, rain=True, is_extreme=False)

cardigan = Clothing(name="Cardigan", gender='b', temp_min=None, temp_max=80, sun=True, snow=True, rain=True, is_extreme=False)
#Add Accessories to List
tops = [tshirts, long_shirt, short_shirt]
#Bottoms of outfits
jeans = Clothing(name="Jeans", gender='b', temp_min=None, temp_max=95, 
                sun=True, snow=True, rain=True, is_extreme=True)

shorts = Clothing(name="Long Sleeved Shirt", gender='b', temp_min=55, 
                  temp_max=None, sun=True, snow=False, rain=False, is_extreme=False)

thermal_underwear = Clothing(name="Thermal Underwear", gender='b', temp_min=35, 
                  temp_max=75, sun=True, snow=True, rain=True, is_extreme=True)
#Add Bottoms to List
bottoms = [jeans, shorts, thermal_underwear]
#Jackets
heavy_coat = Clothing(name="Heavy Coat", gender='b', temp_min=None, 
                  temp_max=60, sun=True, snow=True, rain=True, is_extreme=True)

sweater = Clothing(name="Sweater", gender='b', temp_min=61, 
                  temp_max=78, sun=True, snow=True, rain=True, is_extreme=False)

wool_coat = Clothing(name="Heavy Wool Coat", gender='b', temp_min=None, 
                  temp_max=59, sun=True, snow=True, rain=False, is_extreme=True)

rain_coat = Clothing(name="Rain Coat", gender='b', temp_min=None, temp_max=None, sun=False, snow=True, rain=True, is_extreme=True)
#Add Jackets to List
jackets = [heavy_coat, sweater, wool_coat, rain_coat]
