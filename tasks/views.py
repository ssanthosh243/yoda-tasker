from django.http import HttpResponse
from .models import *
import json
import requests
import paramiko

# Create your views here.


def home(request):
    text = '''<h1 style="text-align: center;"><span style="color: #ff6600;"><em>Welcome to Yoda Tasker<br /></em></span></h1>
<p style="text-align: center;">&nbsp;</p>
<h2 style="text-align: center;"><span style="text-decoration: underline;"><span style="color: #000080;"><em>Useful Links:</em></span></span></h2>
<p style="text-align: center;"><span style="color: #800080;"><em><a style="color: #800080;" title="http://www.jsoneditoronline.org/" href="http://www.jsoneditoronline.org/" target="_blank">http://www.jsoneditoronline.org/</a></em></span></p>
<p style="text-align: center;"><span style="color: #800080;"><em><a style="color: #800080;" title="https://cron-job.org/en/members/" href="https://cron-job.org/en/members/" target="_blank">https://cron-job.org/en/members/</a></em></span></p>'''
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


def shelltask(request, callsign):
    a = ShellTask.objects.get(callsign=callsign)
    b = Host.objects.get(id=a.host_id)

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(a.host, username=b.username, password=b.password)
        stdin, stdout, stderr = ssh.exec_command(a.command)

        data = stdout
        print stdin, stderr

        ssh.close()
        pass
    except Exception, e:
        print (e)
        pass

    return HttpResponse(data)
