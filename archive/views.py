from django.shortcuts import render
from archive.forms import StorageForm
from django.shortcuts import HttpResponse

# Create your views here.
def home_view(request):
    if request.method == 'GET':
        form = StorageForm()
        return render(request, "home.html", {'form' : form})
    elif request.method == 'POST':
        print({k:v for k,v in request.POST.items()})
        return HttpResponse('got it')