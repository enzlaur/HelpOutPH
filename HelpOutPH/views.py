from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse
from google.appengine.ext import db
from models import RescueReport

def home(request):
    if 'fnames' in request.GET:
        r = RescueReport(names = request.GET['fnames'],
                         location = request.GET['flocation'],
                         situation = request.GET['fsituation'],
                         contactinfo = request.GET['fcontact']) 
        r.put()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def report(request):
    return render(request, 'report.html')

def deployedtowhere(request):
    return render(request, 'deployedtowhere.html')

def giverelief(request):
    return render(request, 'giverelief.html')

def listofcauses(request):
    return render(request, 'listofcauses.html')

def reportssubmitted(request):
    rrs = RescueReport.all()
    return render(request, 'reportssubmitted.html', {'rrs':rrs})

def tweettoform(request):
    if 'fnames' in request.GET:
        r = RescueReport(names = request.GET['fnames'],
                         location = request.GET['flocation'],
                         situation = request.GET['fsituation'],
                         contactinfo = request.GET['fcontact']) 
        r.put()
        return render(request, 'tweettoform.html')
    else:
        return render(request, 'tweettoform.html')
  


