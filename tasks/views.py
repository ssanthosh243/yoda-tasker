from django.http import HttpResponse
from .models import *
import json
import requests

# Create your views here.


def home(request):
    text = '''<h1><span style="color: #ff6600;"><em>Welcome to Yoda</em></span></h1>'''
    return HttpResponse(text)


def apitask(request, callsign):
    a = ApiTask.objects.get(callsign=callsign)

    if a.method == 1:
        # GET Method Tasks here
        url = a.url
        headers = a.headers

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = json.dumps(r.json())
            pass
        else:
            data = dict()
            data['error'] = 'Something went wrong !!!'
            data = json.dumps(data)
            pass
        pass

    elif a.method == 2:
        # POST Method Tasks here
        url = a.url
        headers = a.headers
        payload = a.data

        r = requests.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            # data = json.dumps(r.json())
            data = json.dumps({"success": "Command executed successfully !!!"})
            pass
        else:
            data = dict()
            data['error'] = 'Something went wrong !!!'
            data = json.dumps(data)
            pass

        pass

    return HttpResponse(data, content_type='application/json')
