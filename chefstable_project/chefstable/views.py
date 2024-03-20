from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse('<h1> 404: No page bad head </h1>')

def cheque(request):
    return HttpResponse('This is cheque')