from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

def main(request):
    return HttpResponse('<script>location.replace("/Manage/index");</script>')