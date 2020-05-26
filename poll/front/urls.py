from django.urls import path
from front.views import Values_view

urlpatterns = [
    path('',Values_view),
]