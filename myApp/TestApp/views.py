from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#create your views here.
def home(request):
    return HttpResponse("<h2> You just visited home</h2>")

def gallery(request):
    return HttpResponse("<h2>Welcome to Gallery</h2>")

def msg(request):
    return HttpResponse("<h2> You just visited message path</h2>")

def temp_example(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data)) 

data = {
    "name" : "Shyam",
    "age" : "6"
}     

names_dict = {
    "names" : [
        "michael",
        "dean",
        "sam",
        "castiel"
    ]
}

def show_names(request):
    template = loader.get_template('names.html')
    return HttpResponse (template.render(names_dict))