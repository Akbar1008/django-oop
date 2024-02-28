from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
  texts = Post.objects.all()
  return render(request, 'Pages/index.html', {"texts": texts})