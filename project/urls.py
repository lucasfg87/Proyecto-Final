"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index , saludar_a , monstrar_familiares , BuscarFamiliar , AltaFamiliar , ActualizarFamiliar , BorrarFamiliar ,  monstrar_autos , Altadeautos , BuscarAutos , 
                           Altavinos , BuscarVinos , monstrar_vinos , 
                           FamiliarList , FamiliarDetalle , FamiliarCrear ,FamiliarBorrar , FamiliarActualizar)

from argentina.views import index , PostDetalle ,PostList ,PostCrear , PostBorrar, PostActualizar, UserSignUp , UserLogin , UserLogout , AvatarActualizar , UserActualizar ,  MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar , AboutListar 

from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-autos/', monstrar_autos),
    path('mis-autos/buscar', BuscarAutos.as_view()),
    path('mis-autos/alta', Altadeautos.as_view()),
    path('mis-vinos/', monstrar_vinos),
    path('mis-vinos/buscar', BuscarVinos.as_view()),
    path('mis-vinos/alta', Altavinos.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('argentina/', index, name="argentina-index"),
    path('argentina/<int:pk>/detalle/', PostDetalle.as_view(), name="argentina-detalle"),
    path('argentina/listar/',PostList.as_view(), name="argentina-listar"),
    path('argentina/crear/', PostCrear.as_view(), name="argentina-crear"),
    path('argentina/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="argentina-borrar"),
    path('argentina/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="argentina-actualizar"),
    path('argentina/signup/', UserSignUp.as_view(), name = "argentina-signup"),
    path('argentina/login/', UserLogin.as_view(), name= "argentina-login"),
    path('argentina/logout/', UserLogout.as_view(), name="argentina-logout"),
    path('argentina/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="argentina-avatars-actualizar"),
    path('argentina/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="argentina-users-actualizar"),
    path('argentina/mensajes/crear/', MensajeCrear.as_view(), name="argentina-mensajes-crear"),
    path('argentina/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="argentina-mensajes-detalle"),
    path('argentina/mensajes/listar/', MensajeListar.as_view(), name="argentina-mensajes-listar"),
    path('argentina/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="argentina-mensajes-borrar"),
    path('argentina/about/', AboutListar.as_view(), name= "argentina-about"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

