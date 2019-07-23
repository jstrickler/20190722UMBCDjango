from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.



# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to All about Lucky Charms")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to All about Lucky Charms" }
#     return render(request, 'charms/home.html', context)

def index(request):
    return HttpResponse("<h1>Welcome to the Cereals App</h2>")

def magic(request):
    return HttpResponse("<h1>Magically deficient wombats!!</h1>")
