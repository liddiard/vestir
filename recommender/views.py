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
        dates = request.POST.get('dates')
        gender = request.POST.get('gender')
        if dates is None:
            return self.error(error='KeyError', message='Required key (data) '
                              'not found in request.')
        if gender is None:
            return self.error(error='KeyError', message='Required key (gender) '
                              'not found in request.')
        for date in dates:
            urllib2.urlopen('http://api.wunderground.com/api/%s/forecast10day/'
                            'q/%s/%s.json') % (WUNDERGROUND_API_KEY, state, 
                                               city)


boots=Footwear(boots.name = "Boots", boots.gender = 'b', boots.temp_min = None,
               boots.temp_max = 70, boots.sun = True, boots.snow = True, 
               boots.rain = True)

sandals=Footwear(sandals.name = "Sandals", sandals.gender = 'b', 
                 sandals.temp_min=75, sandals.temp_max=None, sandals.sun=True, 
                 sandals.snow=False, sandals.rain = False)

sneakers=Footwear(sneakers.name="Tennis Shoes", sneakers.gender='b', 
                  sneakers.temp_min=50, sneakers.temp_max=None, 
                  sneakers.sun = True, sneakers.snow = False,
                  sneakers.rain = False)

