from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login, name="login"),
    path("citas",views.citas, name="citas"),
    path("contactos",views.contacto,name="contactos")

]
