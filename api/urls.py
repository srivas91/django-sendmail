
from django.urls import path
from api import views
from api.views import contactView, successView
 
urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]