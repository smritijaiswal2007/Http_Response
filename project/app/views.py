from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def http_response(req):
    
    data={'x':True , 'y':False , 'z':None} 
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')
    
    
    
    
    
    # return HttpResponse("Hello")
    # return HttpResponse("<h1> Helllo </h1>")
    # return HttpResponse("<h1 style='color:pink'> Hello Bebo </h1>")
    # data = '<h1> Hello Bebo </h1>'
    # return HttpResponse(data , content_type='text')
    # return HttpResponse(data , content_type='text/plain')
    # return HttpResponse(data , content_type='text/html')
    # for sending json data:
    # content_type = 'text/json'
    
    # python code to json: