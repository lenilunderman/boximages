from django.shortcuts import render

# Import the model to be used for this view and then create the function that will display on the screen.
from .models import ImageGallery

# Create your views here.
def homegallery(request):
    projectsImages = ImageGallery.objects.all() # get all objects from the database
    return render(request,'portfolio/home.html', {'projectsImages': projectsImages})
