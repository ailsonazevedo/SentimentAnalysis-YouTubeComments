from django.shortcuts import render
from sentimentanalysis_npl import sentimentanalysis_npl

# Create your views here.
def home(request):
    return render(request,'index.html')