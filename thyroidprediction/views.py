from django.shortcuts import render
import numpy as np
import joblib as jb
from urllib import request

def home(request):
    return render(request, "home.html")
# Create your views here.
def predict(request):
    sex =(request.GET['sex'])
    on_thyroxine =(request.GET['on_thyroxine'])
    pregnant =(request.GET['pregnant'])
    query_hypothyroid =(request.GET['query_hypothyroid'])
    goitre =(request.GET['goitre'])
    psych =(request.GET['psych'])
    tsh_measured = (request.GET['tsh_measured'])
    tsh = (request.GET['tsh'])
    tt4 = (request.GET['tt4'])
    fti = (request.GET['fti'])
    
    arr=np.array([[sex, on_thyroxine, pregnant,
                   query_hypothyroid, goitre, psych,
                   tsh_measured, tsh, tt4, fti]])
    model=jb.load("thyroidprediction/thyroid_modelrandomf.pkl")
    result=model.predict(arr)[0]
    if result==1:
        return render(request, "index.html", {'data': "You have hypothyroidism"})
    else:
        
        return render(request, "index.html", {'data': "You are normal"})