from django.views.generic import ListView
from .models import Dbapp

# Create your views here.
class HomePageView(ListView):
    model = Dbapp
    template_name = 'home.html'