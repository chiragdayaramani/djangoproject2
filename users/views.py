from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def logout(request):
        response = HttpResponseRedirect('../login')
        response.delete_cookie('sessionid')
        return response