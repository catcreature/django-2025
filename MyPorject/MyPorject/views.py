from django.http import HttpResponse

def hello_new(request):
    return HttpResponse("Hello there.")