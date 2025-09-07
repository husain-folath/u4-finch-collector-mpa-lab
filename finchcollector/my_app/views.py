# my_app/views.py
# Add UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Finch

def finch_index(request):
    finches = Finch.objects.all()  # look familiar?
    return render(request, 'finches/index.html', {'finches': finches})

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a finch by excluding the name field!
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
