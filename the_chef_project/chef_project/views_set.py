from django.http import HttpResponse

def local_host(request):
    return HttpResponse("<h1> Welcome User </h1>")