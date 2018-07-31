from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):




    return render(request,'home.html',locals())
'''

    locals() --> generates a dictionary containing all 

    		variables in the current scope



    # further explore

    globals()

    '''

@login_required(login_url='/accounts/login/')
def riot(request):


    return render(request, 'home.html', locals())
