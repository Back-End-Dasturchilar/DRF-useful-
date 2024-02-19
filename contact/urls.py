from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('contact-info/', ContactInfoView.as_view(), name='contact-info')
]