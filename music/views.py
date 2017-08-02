from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>This is my music app.</h4>")