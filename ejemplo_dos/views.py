from django.shortcuts import render
from django.views.generic import ListView , CreateView 
from ejemplo_dos.models import Post

def index (request):
    return render(request,"ejemplo_dos/index.html",{})

class PostList(ListView):
    model = Post
 
class PostCrear (CreateView):
    model= Post
    success_url = "/ejemplo-dos/listar"
    fields = '__all__'

