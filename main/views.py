from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import VisitorForm
from .models import Visitor

def home(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the visitor's name
            return redirect('welcome')  # Redirect to welcome page
    else:
        form = VisitorForm()
    return render(request, 'main/home.html', {'form': form})
    
def welcome(request):
    return render(request, 'main/welcome.html')

def projects_view(request):
    return render(request, 'projects.html')

def contact_view(request):
    return render(request, 'contact.html')

def index_view(request):
    return render(request, 'main/index.html')