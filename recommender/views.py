import json

from django.views.generic import View
from django.http import HttpResponse, Http404


class AjaxView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax: 
            return super(AjaxView, self).dispatch(*args, **kwargs)
        else:
            raise Http404
        
