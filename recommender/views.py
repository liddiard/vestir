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
