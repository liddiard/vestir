import json

from django.views.generic import View
from django.http import HttpResponse, Http404


class AjaxView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax: 
            return super(AjaxView, self).dispatch(*args, **kwargs)
        else:
            raise Http404
        
    def json_response(self, **kwargs):
        return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
        return self.json_response(result=0, **kwargs)

    def error(self, error_type, message):
        return self.json_response(result=1, error=error_type, message=message)


class RecommendView(AjaxView):
    
    def post(self, request):
        pass


boots=Footwear(name="Boots", gender='b', temp_min=None, temp_max=70, sun=True,
               snow=True, rain=True)

sandals=Footwear(name="Sandals", gender='b', temp_min=75, temp_max=None, 
                 sun=True, snow=False, rain = False)

sneakers=Footwear(name="Tennis Shoes", gender='b', temp_min=50, temp_max=None, 
                  sun=True, snow=False, rain=False)

umbrella = Accessory(name="Umbrella", gender='b', temp_min=None, temp_max=None,
                     sun=False, snow=False, rain=True)

warm_hat = Accessories(name="Warm Hat",gender='b', temp_min=None, temp_max=60, 
                       sun=True, snow=True, rain=False)

scarf = Accessories(name="Scarf", gender='b', temp_min=None, temp_max=60, 
                    sun=True, snow=False, rain=True)

tshirts = Tops(name="T-Shirt", gender='b', temp_min=65, temp_max=None,
               sun=True, snow=False, rain=True)

long_shirt = Tops(name="Long-Sleeved Shirt", gender='b', temp_min=None, 
                  temp_max=75, sun=True, snow=True, rain=True)

short_shirt = Tops(name="Short-Sleeved Shirt", gender='b', temp_min=35, 
                  temp_max=90, sun=True, snow=True, rain=True)

jeans = Bottoms(name="Jeans", gender='b', temp_min=None, temp_max=95, 
                sun=True, snow=True, rain=True)

shorts = Bottoms(name="Long Sleeved Shirt", gender='b', temp_min=55, 
                  temp_max=None, sun=True, snow=False, rain=False)

thermal_underwear = Bottoms(name="Thermal Underwear", gender='b', temp_min=35, 
                  temp_max=75, sun=True, snow=True, rain=True)


heavy_coat = Jackets(name="Heavy Coat", gender='b', temp_min=None, 
                  temp_max=60, sun=True, snow=True, rain=True)

sweater = Jackets(name="Sweater", gender='b', temp_min=61, 
                  temp_max=78, sun=True, snow=True, rain=True)

wool_coat = Jackets(name="Heavy Wool Coat", gender='b', temp_min=None, 
                  temp_max=59, sun=True, snow=True, rain=False)

