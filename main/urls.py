from django.urls import path
from .views import home, welcome
from . import views

urlpatterns = [
    path('', home, name='home'),       # Root URL goes to home view
    path('welcome/', welcome, name='welcome'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'), 
    path('index/', views.index_view, name='home'),  # Map the root URL to the index_view
]