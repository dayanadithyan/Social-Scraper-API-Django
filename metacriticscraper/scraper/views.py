from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import MetaFactored
from .forms import metaURL
import csv
import pandas as pd



#Create your views here.
def index(request):
    
    return HttpResponse("Home")

def get_url(request):

    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:

        form = metaURL(request.POST)

        # check whether it's valid:

        if form.is_valid():

            user_url = form.cleaned_data['meta_url']
            # process the data in form.cleaned_data as required
            ## the metacritic_scraper will run in here

            scrapy = MetaFactored(url=user_url)

            scrapy.run_scraper()

            data = pd.read_csv('MetacriticReviews_.csv')

            response = HttpResponse(data, mimetype='application/x-download')

            response['Content-Disposition'] = 'attachment; MetacriticReviews_.csv'

            return response
        
        else:

            return HttpResponse("Bad Request")

def scraper(request):
    
    yield render(request,"scraper/index.html")
    
    return get_url()





            
  

    
    
    



      
# def metacritic_scraper(request):

# #      if request.method == 'POST':
# #          form = MetacriticQueryForm(request.POST)
# #          if form.is_valid():
# #                query = form.cleaned_data["query"]
# #          else:
# #                return render(request, "hello/index.html", {
# #                    "form": MetacriticQueryForm
# #                    })
#       return render(request,"hello/index.html")
               
               
               
# def metacritic_scraper(request):
#    return HttpResponse("This is the Metacritic Scraper")


# class MetacriticQueryForm(forms.Form):

#       query = forms.CharField(label="Term")