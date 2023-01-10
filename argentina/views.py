from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from argentina.models import Post ,  Avatar , Mensaje , About
from argentina.forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "argentina/index.html", {"posts": posts})

class PostDetalle(DetailView):
    model = Post

class PostList(LoginRequiredMixin, ListView):
    model = Post
 
class PostCrear (CreateView):
    model= Post
    success_url = "/argentina/listar"
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("argentina-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("argentina-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = "/argentina/listar"

class UserLogin(LoginView):
    next_page = "argentina-index"

class UserLogout(LogoutView):
    next_page = "argentina-index"

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = "/argentina/listar"

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('argentina-listar')

# Mendajes 


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("argentina-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("argentina-mensajes-listar")

class  AboutListar(ListView):
    model = About