from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is my Music app homepage</h1>")