from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    ss = '''
        <center>
        
        <h1>hello</h1><hr>
        
        </center>
    
    '''
    
    return HttpResponse(ss)
    
def homepage(request):
    ss='''
    
    <center>
    <h1>homepage</h1>
    </center>
    
    '''
    return HttpResponse(ss)
