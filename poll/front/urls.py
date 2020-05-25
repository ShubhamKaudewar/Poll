from django.urls import path
from front.views import Values_view, create_user

urlpatterns = [
    path('',Values_view),
    path('user/',create_user),
]