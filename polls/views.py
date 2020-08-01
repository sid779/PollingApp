from django.shortcuts import render
from .models import Hackers
import templates
# Create your views here.

# Main page to show candidates for voting
def index(request):
    return render(request,'polls/index.html')